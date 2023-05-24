import os
import sys
import argparse
import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.applications.vgg16 import VGG16

from sklearn.metrics import classification_report

# homemade functions
sys.path.append(os.path.join('utils'))
from file_manage import load_split, save_report
from preprocess import prepare
from plotting import plot_history

def input_parse():
    # initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument('--testing_dataset', type = str, default = "no")
    parser.add_argument('--hidden_layers', type = int, default = 1)
    parser.add_argument('--hidden_units', type = int, default = 12)
    parser.add_argument('--epochs', type = int, default = 2)
    parser.add_argument('--batch_size', type = int, default = 32)
    parser.add_argument('--target_size', type = int, default = 224)
    parser.add_argument('--initial_learning_rate', type = float, default = 0.01)
    parser.add_argument('--decay_steps', type = int, default = 10000)
    parser.add_argument('--decay_rate', type = float, default = 0.9)
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

# load data, train the model, and save model, history, and report
def load_train_save(testing_dataset, hidden_layers, hidden_units, epochs, batch_size, target_size, initial_learning_rate, decay_steps, decay_rate):
    # load fullsize or minisize dataset
    if testing_dataset == "no":
        key_path = os.path.join('data', 'key.csv')
    elif testing_dataset == "yes":
        key_path = os.path.join('data', 'mini_key.csv')

    # load the key 
    df_train, df_test, df_val = load_split(key_path)

    # define target size
    target_size = (target_size, target_size)

    # prepare the data
    train_images, val_images, test_images = prepare(df_test, df_train, df_val, target_size, batch_size)

    # load model without classifier layers
    model = VGG16(include_top = False, 
                  pooling = 'avg', 
                  input_shape = (224, 224, 3))

    # mark loaded layers as not trainable
    for layer in model.layers:
        layer.trainable = False

    # add new classifier layers
    flat = Flatten()(model.layers[-1].output)

    # add one or two hidden layers
    if hidden_layers == 1:
        class1 = Dense(hidden_units, activation = 'relu')(flat)
        output = Dense(15, activation = 'softmax')(class1)
    elif hidden_layers == 2:
        class1 = Dense(hidden_units, activation = 'relu')(flat)
        class2 = Dense(hidden_units, activation = 'relu')(class1)
        output = Dense(15, activation = 'softmax')(class2)

    # define new model
    model = Model(inputs = model.inputs, 
                  outputs = output)

    # define the learning rate schedule
    lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate = initial_learning_rate,
        decay_steps = decay_steps,
        decay_rate = decay_rate,)

    # define the optimizer
    sgd = SGD(learning_rate = lr_schedule)

    # compile the model
    model.compile(optimizer = sgd,
                  loss = 'categorical_crossentropy',
                  metrics = ['accuracy'])

    # fit the model
    H = model.fit(train_images, 
                steps_per_epoch = len(train_images),
                validation_data = val_images,
                validation_steps = len(val_images),
                epochs = epochs,
                batch_size = batch_size,
                verbose = 1)

    # save plot of the history
    plot_history(H, epochs, os.path.join('results', 'history.png'))

    # save the report
    save_report(model, test_images, train_images, df_test, os.path.join('results', 'report.txt'))

    # save the model
    model.save(os.path.join('results', 'model'))

if __name__ == '__main__':
    args = input_parse()
    load_train_save(args.testing_dataset, args.hidden_layers, args.hidden_units, args.epochs, args.batch_size, args.target_size, args.initial_learning_rate, args.decay_steps, args.decay_rate)