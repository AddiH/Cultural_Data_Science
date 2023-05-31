import os
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
import scipy.sparse as sp
import pandas as pd
from joblib import dump

def logistic_regression():
    # message
    print("Running logistic regression...")
    # load data 
    X_train_feats = sp.load_npz(os.path.join("in", 'X_train_feats.npz'))
    X_test_feats  = sp.load_npz(os.path.join("in", 'X_test_feats.npz'))
    y_train = pd.read_csv(os.path.join("in", "y_train.csv")).squeeze(1)
    y_test = pd.read_csv(os.path.join("in", "y_test.csv")).squeeze(1)

    # instantiate the classifier
    classifier = LogisticRegression().fit(X_train_feats, y_train)

    # fit the classifier
    classifier.fit(X_train_feats, y_train) # train the model
    y_pred = classifier.predict(X_test_feats) # predict on the test data

    # get classification report
    classifier_metrics = metrics.classification_report(y_test, y_pred) 

    # save the report to a file
    with open(os.path.join("out", "logistic_regression_classification_report.txt"), "w") as f:
        f.write(classifier_metrics)
    # save the model
    dump(classifier, os.path.join("models", "logistic_regression_classifier.joblib"))
    return None

def main():
    # run logistic regression. Simple with no arguments
    logistic_regression()

# if this code is called from command line, run main
if __name__ == "__main__":
    main()