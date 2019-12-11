from sklearn.preprocessing import LabelEncoder
from keras.utils.np_utils import to_categorical
import numpy as np 

def flat_list(L):
    return [i for sublist in L for i in sublist]

test = [['I am jason'],['hello you are jason']] # test data 
vocab = np.unique(" ".join(flat_list(test)).split()) # list of unique vocab in our data 

# Label Encoding
encoder = LabelEncoder() # encode class values as integers
encoder.fit(vocab)
encoded_Y = encoder.transform(vocab)
# one hot encoding 
one_hot_y = to_categorical(encoded_Y, dtype='int')

# MAIN 
alpha = .5 # constant forgetting factor 

def fofe_vectorizer(seq_len): 
    '''
    input seq = length of sequence 
    '''
    forget_vec = np.zeros(seq_len)
    for index, i in enumerate(reversed(range(seq_len))):     
        forget_vec[index] = alpha ** i
    return forget_vec.reshape((1,seq_len))

def sequence_encoder(seq):
    '''
    input seq = sequence of strings 
    '''
    return to_categorical(encoder.transform(seq.split()),num_classes=len(vocab))
    
def fofe_matrix(data): 
    '''
    input seq = list of sequence of strings 
    '''
    M = np.zeros((len(data), len(vocab)))                   
    
    for index,i in enumerate(data): 
        seq_len = len(i[0].split())
        fofe_constant = fofe_vectorizer(seq_len)
        seq_to_num = sequence_encoder(i[0])
        fofe_vec = np.matmul(fofe_constant,seq_to_num)
        M[index] = fofe_vec
    return M

fm = fofe_matrix(test)

# print(list(zip(test, fm)))

print('original text:',test[0])
print('fofe matrix:',fm[0])


