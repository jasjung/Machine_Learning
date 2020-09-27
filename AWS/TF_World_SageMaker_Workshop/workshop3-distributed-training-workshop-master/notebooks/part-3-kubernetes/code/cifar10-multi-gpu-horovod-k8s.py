import tensorflow as tf

import horovod.tensorflow.keras as hvd

from datetime import datetime
import argparse
import os
import numpy as np
import codecs
import json

import tensorflow.keras.backend as K
from tensorflow import keras
from tensorflow.keras.layers import Input, Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.utils import multi_gpu_model
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint
from model_def import get_model
    
HEIGHT = 32
WIDTH  = 32
DEPTH  = 3
NUM_CLASSES = 10
NUM_TRAIN_IMAGES = 40000
NUM_VALID_IMAGES = 10000
NUM_TEST_IMAGES  = 10000

def train_preprocess_fn(image):

    # Resize the image to add four extra pixels on each side.
    image = tf.image.resize_image_with_crop_or_pad(image, HEIGHT + 8, WIDTH + 8)

    # Randomly crop a [HEIGHT, WIDTH] section of the image.
    image = tf.random_crop(image, [HEIGHT, WIDTH, DEPTH])

    # Randomly flip the image horizontally.
    image = tf.image.random_flip_left_right(image)

    return image


def make_batch(filenames, batch_size):
    """Read the images and labels from 'filenames'."""
    # Repeat infinitely.
    dataset = tf.data.TFRecordDataset(filenames).repeat()

    # Parse records.
    dataset = dataset.map(single_example_parser, num_parallel_calls=1)

    # Batch it up.
    dataset = dataset.batch(batch_size, drop_remainder=True)
    iterator = dataset.make_one_shot_iterator()

    image_batch, label_batch = iterator.get_next()
    return image_batch, label_batch


def single_example_parser(serialized_example):
    """Parses a single tf.Example into image and label tensors."""
    # Dimensions of the images in the CIFAR-10 dataset.
    # See http://www.cs.toronto.edu/~kriz/cifar.html for a description of the
    # input format.
    features = tf.parse_single_example(
        serialized_example,
        features={
            'image': tf.FixedLenFeature([], tf.string),
            'label': tf.FixedLenFeature([], tf.int64),
        })
    image = tf.decode_raw(features['image'], tf.uint8)
    image.set_shape([DEPTH * HEIGHT * WIDTH])

    # Reshape from [depth * height * width] to [depth, height, width].
    image = tf.cast(
        tf.transpose(tf.reshape(image, [DEPTH, HEIGHT, WIDTH]), [1, 2, 0]),
        tf.float32)
    label = tf.cast(features['label'], tf.int32)
    
    image = train_preprocess_fn(image)
    label = tf.one_hot(label, NUM_CLASSES)
    
    return image, label

def save_history(path, history):

    history_for_json = {}
    # transform float values that aren't json-serializable
    for key in list(history.history.keys()):
        if type(history.history[key]) == np.ndarray:
            history_for_json[key] == history.history[key].tolist()
        elif type(history.history[key]) == list:
           if  type(history.history[key][0]) == np.float32 or type(history.history[key][0]) == np.float64:
               history_for_json[key] = list(map(float, history.history[key]))

    with codecs.open(path, 'w', encoding='utf-8') as f:
        json.dump(history_for_json, f, separators=(',', ':'), sort_keys=True, indent=4) 


def main(args):
    # Hyper-parameters
    epochs = args.epochs
    lr = args.learning_rate
    batch_size = args.batch_size
    momentum = args.momentum
    weight_decay = args.weight_decay
    optimizer = args.optimizer

    # Data directories and other options
    gpu_count = args.gpu_count
    model_dir = args.model_dir
    training_dir = args.train
    validation_dir = args.validation
    eval_dir = args.eval
    
    # Change 2
    hvd.init()
    size = hvd.size()
    
    # Change 3 - pin GPU to be used to process local rank (one GPU per process)
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    config.gpu_options.visible_device_list = str(hvd.local_rank())
    K.set_session(tf.Session(config=config))
    
    train_dataset = make_batch(training_dir+'/train.tfrecords',  batch_size)
    val_dataset = make_batch(validation_dir+'/validation.tfrecords', batch_size)
    eval_dataset = make_batch(eval_dir+'/eval.tfrecords', batch_size)
    
    input_shape = (HEIGHT, WIDTH, DEPTH)
    
    # Change 4 - update learning rate
    # Change 5 - update training code
    
    # Change 6 - update callbacks - sync initial state, checkpoint only on 1st worker
    callbacks = []
    callbacks.append(hvd.callbacks.BroadcastGlobalVariablesCallback(0))
    callbacks.append(hvd.callbacks.MetricAverageCallback())
    callbacks.append(hvd.callbacks.LearningRateWarmupCallback(warmup_epochs=5, verbose=1))
    callbacks.append(tf.keras.callbacks.ReduceLROnPlateau(patience=10, verbose=1))
    if hvd.rank() == 0:
        callbacks.append(ModelCheckpoint(args.output_data_dir + '/checkpoint-{epoch}.h5'))
        logdir = args.output_data_dir + '/' + datetime.now().strftime("%Y%m%d-%H%M%S")
        callbacks.append(TensorBoard(log_dir=logdir, profile_batch=0))
    
    model = get_model(lr, weight_decay, optimizer, momentum, hvd)

    # Train model
    history = model.fit(x=train_dataset[0], y=train_dataset[1],
                        steps_per_epoch= (NUM_TRAIN_IMAGES // batch_size)// size,
                        validation_data=val_dataset,
                        validation_steps= (NUM_VALID_IMAGES // batch_size)// size,
                        epochs=epochs, callbacks=callbacks)

    # Evaluate model performance
    score = model.evaluate(eval_dataset[0],
                           eval_dataset[1],
                           steps=NUM_TEST_IMAGES // args.batch_size,
                           verbose=0)
    print('Test loss    :', score[0])
    print('Test accuracy:', score[1])

    if hvd.rank() == 0:
        save_history(args.output_data_dir + "/hvd_history.p", history)
        # Save model to model directory
        #bug: https://github.com/horovod/horovod/issues/1437
        #tf.contrib.saved_model.save_keras_model(model, args.model_output_dir)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    # Hyper-parameters
    parser.add_argument('--epochs',        type=int,   default=15)
    parser.add_argument('--learning-rate', type=float, default=0.001)
    parser.add_argument('--batch-size',    type=int,   default=256)
    parser.add_argument('--weight-decay',  type=float, default=2e-4)
    parser.add_argument('--momentum',      type=float, default='0.9')
    parser.add_argument('--optimizer',     type=str,   default='adam')

    # Data directories and other options
    parser.add_argument('--gpu-count',        type=int,   default=0)
    parser.add_argument('--train',            type=str)
    parser.add_argument('--validation',       type=str)
    parser.add_argument('--eval',             type=str)
    
    parser.add_argument('--model_dir',        type=str)
    parser.add_argument('--model_output_dir', type=str)
    parser.add_argument('--output_data_dir',  type=str)
    parser.add_argument('--tensorboard_dir',  type=str)
    
    args = parser.parse_args()
    main(args)
