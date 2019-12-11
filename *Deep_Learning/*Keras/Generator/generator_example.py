# python genrator_example.py 


###############################################################
# Packages 
###############################################################
# import packages 
import sys
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import pickle 
import zipfile
import datetime 
import subprocess
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,LabelBinarizer,OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.metrics import accuracy_score, f1_score
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.utils import to_categorical
# information 
print('Python Version:', sys.version[:3])
print('Date:',datetime.datetime.now())


###############################################################
# Functions 
###############################################################
def count_data_set(path): 
    '''
    input: path to the file 
    '''
    # use bash command to get the count directly 
    output = subprocess.check_output(("wc -l %s" % path).split()
        ,universal_newlines=True)
    # extract the count only and subtract header    
    return int(output.split()[0]) - 1   


def extract_unique_labels(path): 
    '''
    input: path to the file 
    output: list of unique labels that are integers 
    '''
    output = subprocess.check_output("cut -d',' -f1 %s | sort | uniq" % path, 
        universal_newlines=True,shell=True).split()  
    unique_label = []
    for i in output: 
        # convert string to int 
        try: unique_label.append(int(i))
        # excluding non integer values 
        except: continue 
    return unique_label


def count_features(path): 
    '''
    input: path to the file 
    output: count number of features in csv
    '''
    output = subprocess.check_output("head -1 %s | sed 's/[^,]//g' | wc -c" % path, 
                           universal_newlines=True,shell=True)
    return int(output.split()[0])-1


def read_labels(path):
    '''
    goal: extracting just the label from a file for 
            performance measurement. 
    '''
    # open file for reading 
    f = open(path, "r")
    # skip the header first line 
    next(f)
    # list to store true labels 
    testLabels=[]
    # loop over the lines in the testing file
    for line in f:
        # extract the class label, update the test labels list, and
        # increment the total number of testing images
        label = int(line.strip().split(",")[0])
        testLabels.append(label)
    return testLabels


def performance(y_true,y_pred): 
    accuracy = accuracy_score(y_true,y_pred)
    roc_auc = roc_auc_score(y_true, y_pred)
    pr_auc = average_precision_score(y_true, y_pred)
    return accuracy, roc_auc, pr_auc 
    

def csv_generator(inputPath, bs, lb, mode="train"):
    '''
    output: generator object for keras to ingest 
    '''
    # open the CSV file for reading
    f = open(inputPath, "r")
    # skip the header first line 
    next(f) 
    # loop indefinitely 
    while True:
        # initialize our batches of records and labels
        records = []
        labels = []
        # keep looping until we reach our batch size
        while len(records) < bs:
            # attempt to read the next line of the CSV file
            line = f.readline()
            # check to see if the line is empty, indicating we have
            # reached the end of the file
            if line == "":
                # reset the file pointer to the beginning of the file
                # and re-read the line
                f.seek(0)
                # skip the header first line 
                next(f)
                line = f.readline()
                # if we are evaluating we should now break from our
                # loop to ensure we don't continue to fill up the
                # batch from samples at the beginning of the file
                if mode == "eval":
                    break
            # extract the label and construct the record
            line = line.strip().split(",")
            # label is in the first column of the data 
            label = line[0]
            record = np.array([float(x) for x in line[1:]],dtype='float32')
            # update our corresponding batches lists
            records.append(record)
            labels.append(label)
        # one-hot encode the labels
        labels = to_categorical(np.array(labels),2)
        # yield the batch to the calling function
        yield (np.array(records), labels)


def model_training(TRAIN_CSV, VAL_CSV, TEST_CSV, NUM_EPOCHS, BS): 
    '''
    goal: trains keras model. 
    '''
    lb=None # change this later. placeholder for future labelbinarizer.  

    # read test label for performance measurement 
    y_true = read_labels(TEST_CSV)

    # get data count 
    NUM_TRAIN_SET = count_data_set(path=TRAIN_CSV)
    NUM_TEST_SET = count_data_set(path=TEST_CSV)
    NUM_VAL_SET = count_data_set(path=VAL_CSV)
    print('NUM_TRAIN_SET,NUM_VAL_SET,NUM_TEST_SET:',
        NUM_TRAIN_SET,NUM_VAL_SET,NUM_TEST_SET)

    # extract unique labels 
    unique_label = extract_unique_labels(path=TEST_CSV)
    print('unique_label:',unique_label)

    # extract number of feature size 
    feature_size = count_features(TEST_CSV)
    print('feature_size:',feature_size)

    # initialize both the train, val, test csv generators
    trainGen = csv_generator(TRAIN_CSV, BS, lb, mode="train")
    valGen = csv_generator(VAL_CSV, BS, lb, mode="train")
    testGen = csv_generator(TEST_CSV, BS, lb, mode="eval")

    # init keras model 
    model = Sequential()
    model.add(Dense(256, input_shape=(feature_size,), activation='relu'))
    model.add(Dense(len(unique_label), activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()

    print("[INFO] training w/ generator...")
    history = model.fit_generator(
                            trainGen,
                            steps_per_epoch=np.ceil(NUM_TRAIN_SET/BS),
                            validation_data=valGen,
                            validation_steps=np.ceil(NUM_VAL_SET/BS),
                            epochs=NUM_EPOCHS)

    # make predictions on the testing images, finding the index of the
    # label with the corresponding largest predicted probability
    y_pred = model.predict_generator(testGen, 
                            steps=np.ceil(NUM_TEST_SET/BS)) # predIdxs
    y_pred = list(np.argmax(y_pred, axis=1))
    # ceil(num_samples / batch_size)

    # show a nicely formatted classification report
    # print("[INFO] evaluating network...")
    # print(classification_report(np.array(testLabels), predIdxs,target_names=unique_label))

    # Performance
    accuracy, roc_auc, pr_auc = performance(y_true,y_pred)
    print('ACCURACY:', accuracy)
    print(' ROC AUC:', roc_auc)
    print('  PR AUC:', pr_auc)

    return model, history, y_pred


def main(): 
    # define the paths to CSV files
    TRAIN_CSV = "data/train.csv"
    TEST_CSV = "data/test.csv"
    VAL_CSV = "data/val.csv"

    # initialize the number of epochs to train for and batch size
    NUM_EPOCHS = 2
    BS = 32

    # train model 
    model,history,ypred = model_training(
        TRAIN_CSV=TRAIN_CSV
        ,VAL_CSV=VAL_CSV
        ,TEST_CSV=TEST_CSV
        ,NUM_EPOCHS=NUM_EPOCHS
        ,BS=BS)


if __name__ == "__main__":
    main()
    print('done')
