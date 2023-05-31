import numpy as np
import os
import sys
import argparse

sys.path.append(os.path.join('utils'))
from utils import create_model

def input_parse():
    # initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--folder_path', type=str, default="first_try")
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

def train(epochs, batch_size, folder_path):
    # Load variables from a file
    file_path = os.path.join("in", folder_path, "data.npz")
    with np.load(file_path) as data:
        predictors = data['predictors']
        label = data['label']
        max_sequence_len = data['max_sequence_len']
        total_unique_words = data['total_unique_words']

    # initialize the model
    model = create_model(max_sequence_len, total_unique_words)

    # train the model
    history = model.fit(predictors, 
                        label, 
                        epochs=epochs, 
                        batch_size=batch_size, 
                        verbose=1) 

    # Create a new directory
    save_dir = os.path.join("models", folder_path)

    # Check if the directory already exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Save the model
    model.save(save_dir)

def main():
    args = input_parse()
    train(args.epochs, args.batch_size, args.folder_path)

if __name__ == "__main__":
    main()