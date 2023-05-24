import os
import argparse
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
import scipy.sparse as sp
import pandas as pd
from joblib import dump
import numpy as np

def input_parse():
    #initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--activation", type = str, default = "logistic") # activation function
    parser.add_argument("--hidden_layer_sizes", type = tuple, default = (20,)) # hidden layer sizes
    parser.add_argument("--max_iter", type = int, default = 1000) # max iterations
    parser.add_argument("--random_state", type = int, default = 69) # random state
    parser.add_argument("--learning_rate", type = str, default = "adaptive") # learning rate
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

def neural_net(activation, hidden_layer_sizes, max_iter, random_state, learning_rate):
    # string with parameters
    string_parameters = f"Neural net with activation = {activation}, hidden_layer_sizes = {hidden_layer_sizes}, max_iter = {max_iter}, random_state = {random_state}, learning_rate = {learning_rate}"
    # print parameters
    print(string_parameters)

    # load data 
    X_train = np.load(os.path.join("in", 'X_train.npy'))
    X_test  = np.load(os.path.join("in", 'X_test.npy'))
    y_train = np.load(os.path.join("in", "y_train.npy"))
    y_train = np.ravel(y_train) # reshape y_train to a 1D array
    y_test =  np.load(os.path.join("in", "y_test.npy"))
    y_test = np.ravel(y_test) # reshape y_test to a 1D array

    # instantiate the classifier
    classifier = MLPClassifier(activation = activation, 
                               hidden_layer_sizes = hidden_layer_sizes, 
                               max_iter = max_iter,  
                               random_state = random_state,
                               learning_rate = learning_rate, 
                               early_stopping=True,
                               verbose=True)


    # fit the classifier
    classifier.fit(X_train, y_train) # train the model
    y_pred = classifier.predict(X_test) # predict on the test data

    # get classification report
    classifier_metrics = metrics.classification_report(y_test, y_pred) 

    # save the report to a file
    with open(os.path.join("out", "MLPClassifier_report.txt"), "w") as f:
        f.write(classifier_metrics)
    # save the model
    dump(classifier, os.path.join("models", "MLPClassifier.joblib"))
    # save the parameters
    with open(os.path.join("models", "MLP_parameters.txt"), "w") as f:
        f.write(string_parameters)
    return None

def main():
    # run input parse to get name
    args = input_parse()
    # pass args to function
    neural_net(args.activation, args.hidden_layer_sizes, args.max_iter, args.random_state, args.learning_rate)

# if this code is called from command line, run main
if __name__ == "__main__":
    main()