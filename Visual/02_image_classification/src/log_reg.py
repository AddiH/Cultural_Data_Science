import os
import argparse
import numpy as np
from joblib import dump
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

def input_parse():
    #initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--penalty", type = str, default = "none") 
    parser.add_argument("--tol", type = float, default = 0.1) 
    parser.add_argument("--solver", type = str, default = "saga") 
    parser.add_argument("--multi_class", type = str, default = "multinomial") 
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

def log_reg(penalty, tol, solver, multi_class):
    # string with parameters
    string_parameters = f"Logistic regression classifier with penalty = {penalty}, tol = {tol}, solver = {solver}, multi_class = {multi_class}"
    # print parameters
    print(string_parameters)

    # load data 
    X_train = np.load(os.path.join("in", 'X_train.npy'))
    X_test  = np.load(os.path.join("in", 'X_test.npy'))
    y_train = np.load(os.path.join("in", "y_train.npy"))
    y_train = np.ravel(y_train) # reshape y_train to a 1D array
    y_test =  np.load(os.path.join("in", "y_test.npy"))
    y_test = np.ravel(y_test) # reshape y_train to a 1D array

    # instantiate the classifier
    clf = LogisticRegression(penalty = penalty,
                        tol = tol,
                        verbose = True, 
                        solver = solver,
                        multi_class = multi_class)

    # fit the classifier
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # get classification report
    classifier_metrics = metrics.classification_report(y_test, y_pred)

    # save the report to a file
    with open(os.path.join("out", "LogisticRegression_report.txt"), "w") as f:
        f.write(classifier_metrics)
    # save the model
    dump(clf, os.path.join("models", "LogisticRegression.joblib"))
    # save the parameters
    with open(os.path.join("models", "LogisticRegression_parameters.txt"), "w") as f:
        f.write(string_parameters)
    return None

def main():
    # get the arguments
    args = input_parse()
    # run the neural net
    log_reg(args.penalty, args.tol, args.solver, args.multi_class)

if __name__ == "__main__":
    main()