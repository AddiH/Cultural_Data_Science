import pandas as pd
import os
import numpy as np
from sklearn.metrics import classification_report

def load_split(path):
    '''
    Load the key.csv file and split it into train, test, and val sets.
    '''
    # load the df 
    df = pd.read_csv(path)

    # split the df into train, test, and val sets
    df_train = df[df['dataset'] == 'train']
    df_test = df[df['dataset'] == 'test']
    df_val = df[df['dataset'] == 'val']

    return df_train, df_test, df_val

def save_report(model, test_images, train_images, df_test, save_path):
    '''
    Make and save the classification report to a txt file.
    '''
    # Predict the label of the test_images
    pred = model.predict(test_images)
    pred = np.argmax(pred,axis=1)

    # Map the label
    labels = (train_images.class_indices)
    labels = dict((v,k) for k,v in labels.items())
    pred = [labels[k] for k in pred]
    y_test = list(df_test.class_label)

    report = classification_report(y_test, pred)
    # Save the report
    with open(save_path, 'w') as f:
        f.write(report)