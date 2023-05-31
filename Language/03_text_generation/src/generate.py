import os
import sys
import numpy as np
import argparse
import tensorflow as tf
from keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences

sys.path.append(os.path.join('utils'))
from utils import generate_text

def input_parse():
    # initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument('--prompt', type=str, default="I am", help="The prompt to start the text generation with.")
    parser.add_argument('--length', type=int, default=10, help="The length of the generated text.")
    parser.add_argument('--folder_path', type=str, default="first_try")
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

def generate(prompt, length, folder_path):
    # load data
    file_path = os.path.join("in", folder_path, "data.npz")

    with np.load(file_path) as data:
        max_sequence_len = data['max_sequence_len']

    # load tokenizer
    token_path = os.path.join("in", folder_path, "tokenizer.json")
    with open(token_path, 'r', encoding='utf-8') as f:
        tokenizer_json = f.read()
    tokenizer = tokenizer_from_json(tokenizer_json)

    # convert tokenizer JSON string to a tokenizer object
    tokenizer = tokenizer_from_json(tokenizer_json)

    # path to model
    model_path = os.path.join("models", folder_path)

    # load model
    model = tf.keras.models.load_model(model_path)

    # generate text
    print(generate_text(prompt, length, model, max_sequence_len, tokenizer))

def main():
    # get variables
    args = input_parse()
    # generate text
    generate(args.prompt, args.length, args.folder_path)

if __name__ == "__main__":
    main()