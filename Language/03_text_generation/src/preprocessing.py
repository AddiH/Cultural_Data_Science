import os
import re
import sys
import argparse
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer

sys.path.append(os.path.join('utils'))
from utils import get_sequence_of_tokens, generate_padded_sequences

def input_parse():
    # initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument('--testing_dataset', type=str, default="no", choices=["yes", "no"],
        help="Run the model on a small dataset to test it. Options: yes/no")
    parser.add_argument('--max_dictionary_size', type=int, default=None,
        help="The maximum number of words to keep, in the dictionary. Only the most common num_words-1 words will be kept. Default: None, all words are kept.")
    parser.add_argument('--folder_path', type=str, default="first_try")
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

def prepare(testing_dataset, max_dictionary_size, folder_path):
    # print message for user
    print("[INFO] Preparing data...")
    #print("[INFO] Loading data...")
    # go through all .csv files in data/ and append them to df
    corpus = []
    for file in os.listdir("data"):
        if file.endswith(".csv"): # avoid the zip file
            file_path = os.path.join("data", file) # path to file
            csv = pd.read_csv(file_path, usecols=['commentBody']) # read only one column of the csv file
            comments = csv['commentBody'].tolist() # convert to list
            for comment in comments: # for each comment
                # if comment is a string and not null/nan/NA, append it to corpus
                if isinstance(comment, str) and not pd.isnull(comment):
                    corpus.append(comment)

    # if relevant, use only the first 10 comments
    if testing_dataset == "yes":
        corpus = corpus[:10]
    elif testing_dataset == "no":
        corpus = corpus

    # Remove the <br/> tags
    corpus = [re.sub(r'<br/>', ' ', comment) for comment in corpus]

    #print("[INFO] Tokenize the data...")
    # Tokenize (and clean) the corpus - this takes a while
    tokenizer = Tokenizer(num_words = max_dictionary_size)
    tokenizer.fit_on_texts(corpus)
    total_unique_words = len(tokenizer.word_index) + 1 

    #print("[INFO] Padding sequences...")
    # Convert data to sequence of tokens
    input_sequences = get_sequence_of_tokens(tokenizer, corpus)
    # Pad the sequences
    predictors, label, max_sequence_len = generate_padded_sequences(input_sequences, total_unique_words)

    # Create a new directory
    in_dir = os.path.join("in", folder_path)

    # Check if the directory already exists
    if not os.path.exists(in_dir):
        os.makedirs(in_dir)

    # Save path
    save_path = os.path.join(in_dir, "data.npz")

    # save variables to a file
    np.savez(save_path, 
            predictors = predictors, 
            label = label, 
            max_sequence_len = max_sequence_len, 
            total_unique_words = total_unique_words)

    # save path
    save_path_tokenizer = os.path.join(in_dir, "tokenizer.json")

    # save tokenizer to file 
    with open(save_path_tokenizer, 'w', encoding='utf-8') as f:
        f.write(tokenizer.to_json())

def main():
    # get the variables
    args = input_parse()
    # prepare the data
    prepare(args.testing_dataset, args.max_dictionary_size, args.folder_path)

if __name__ == "__main__":
    main()