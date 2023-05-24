import os
import sys
import argparse
import pandas as pd
import numpy as np

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.applications.vgg16 import VGG16

from sklearn.metrics import classification_report

# homemade functions
sys.path.append(os.path.join('utils'))
from homemade_functions import data_flow
from plotting import plot_history


def input_parse():
    # initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument('--testing_dataset', type=str, default="no", choices=["yes", "no"],
                        help="Specify whether to use a subset of the data for testing the code. (Options: yes, no)")
    parser.add_argument('--hidden_layers', type=int, default=1, choices=[1, 2],
                        help="Specify the number of hidden layers. (Options: 1, 2)")
    parser.add_argument('--hidden_units_1', type=int, default=12,
                        help="Specify the number of units in the first hidden layer.")
    parser.add_argument('--hidden_units_2', type=int, default=12,
                        help="Specify the number of units in the second hidden layer.")
    parser.add_argument('--epochs', type=int, default=2,
                        help="Specify the number of training epochs.")
    parser.add_argument('--batch_size', type=int, default=32,
                        help="Specify the batch size for training.")
    parser.add_argument('--initial_learning_rate', type=float, default=0.01,
                        help="Specify the learning rate for training.")
    parser.add_argument('--decay_steps', type=int, default=10000,
                        help="Specify the decay steps for training.")
    parser.add_argument('--decay_rate', type=float, default=0.9,    
                        help="Specify the decay rate for training.")
    parser.add_argument('--target_size', type=int, default=244,
                        help="Specify the target size for the images. Eg. 244 will become: (244, 244)")

    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

# load data, train the model, and save model, history, and report
def load_train_save(testing_dataset, hidden_layers, hidden_units_1, hidden_units_2, epochs, batch_size, initial_learning_rate, decay_steps, decay_rate, target_size):

    # load fullsize or minisize dataset
    if testing_dataset == "no":
        df_train = pd.read_csv(os.path.join('data', 'train.csv'))
        df_test = pd.read_csv(os.path.join('data', 'test.csv'))
        df_val = pd.read_csv(os.path.join('data', 'val.csv'))
    elif testing_dataset == "yes":
        df_train = pd.read_csv(os.path.join('data', 'mini_train.csv'))
        df_test = pd.read_csv(os.path.join('data', 'mini_test.csv'))
        df_val = pd.read_csv(os.path.join('data', 'mini_val.csv'))

    # prepare the data
    target_size = (target_size, target_size)
    test_images, train_images, val_images = data_flow(df_test, df_train, df_val, target_size, batch_size)

    # load model without classifier layers
    model = VGG16(include_top = False, 
                    pooling = 'avg', 
                    input_shape = (224, 224, 3))

    # mark loaded layers as not trainable
    for layer in model.layers:
        layer.trainable = False

    # add new classifier layers
    flat = Flatten()(model.layers[-1].output)
    class1 = Dense(hidden_units_1, activation = 'relu')(flat)

    # add one or two hidden layers
    if hidden_layers == 1:
        output = Dense(18, activation = 'softmax')(class1)
    elif hidden_layers == 2:
        class2 = Dense(hidden_units_2, activation = 'relu')(class1)
        output = Dense(18, activation = 'softmax')(class2)

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

    # print message
    print("[INFO] Training completed.")

    # save plot of the history
    plot_history(H, epochs, os.path.join('results', 'plots', 'history.png'))

    # save the model
    model.save(os.path.join('results', 'model'))

if __name__ == '__main__':
    args = input_parse()
    load_train_save(args.testing_dataset, args.hidden_layers, args.hidden_units_1, args.hidden_units_2, args.epochs, args.batch_size, args.initial_learning_rate, args.decay_steps, args.decay_rate, args.target_size)