import os
import argparse
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
import scipy.sparse as sp
import pandas as pd
from joblib import dump

def input_parse():
    #initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--activation", type = str, default = "logistic") # activation function
    ### PROBLEM: hidden_layer_sizes is a tuple, how to parse it from command line? ###
    parser.add_argument("--hidden_layer_sizes", nargs='+', type=int, default=[20,10]) # hidden layer sizes
    parser.add_argument("--max_iter", type = int, default = 10) # max iterations
    parser.add_argument("--random_state", type = int, default = 69) # random state
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

def neural_net(activation, hidden_layer_sizes, max_iter, random_state):
    # changing hidden_layer_sizes list to tuple
    hidden_layer_sizes = tuple(hidden_layer_sizes)
    
    # string with parameters
    string_parameters = f"Running neural net with activation = {activation}, hidden_layer_sizes = {hidden_layer_sizes}, max_iter = {max_iter}, random_state = {random_state}"
    # print parameters
    print(string_parameters)

    # load data 
    X_train_feats = sp.load_npz(os.path.join("in", 'X_train_feats.npz'))
    X_test_feats  = sp.load_npz(os.path.join("in", 'X_test_feats.npz'))
    y_train = pd.read_csv(os.path.join("in", "y_train.csv")).squeeze(1)
    y_test = pd.read_csv(os.path.join("in", "y_test.csv")).squeeze(1)

    # instantiate the classifier
    classifier = MLPClassifier(activation = activation, 
                               hidden_layer_sizes = hidden_layer_sizes, 
                               max_iter = max_iter,  
                               random_state = random_state)

    # fit the classifier
    classifier.fit(X_train_feats, y_train) # train the model
    y_pred = classifier.predict(X_test_feats) # predict on the test data

    # get classification report
    classifier_metrics = metrics.classification_report(y_test, y_pred) 

    # save the report to a file
    with open(os.path.join("out", "MLPClassifier_report.txt"), "w") as f:
        f.write(classifier_metrics)
    # save the model and the vectorizer
    dump(classifier, os.path.join("models", "MLPClassifier.joblib"))
    # save the parameters
    with open(os.path.join("models", "MLP_parameters.txt"), "w") as f:
        f.write(string_parameters)
    return None

def main():
    # run input parse to get name
    args = input_parse()
    # pass args to function
    neural_net(args.activation, args.hidden_layer_sizes, args.max_iter, args.random_state)

# if this code is called from command line, run main
if __name__ == "__main__":
    main()
