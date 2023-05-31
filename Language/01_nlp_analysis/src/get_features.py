import os
import re
import sys
import spacy
import pandas as pd
from tqdm import tqdm
import argparse
sys.path.append(os.path.join('utils'))
from nlp_counter import nlp_counter # this is a function made specifically for this assignment

def input_parse():
    # initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--data_path", type = str, default = os.path.join("in", "USEcorpus")) # default data folder
    parser.add_argument("--spacy_model", type = str, default = "en_core_web_md") # default spacy model
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args


def feature_extraction(data_path, spacy_model):
    '''
    Takes a path to a folder with subfolders containing .txt files.
    Extracts lingustic features from the text and saves the results from each folder in csv format.
    '''
    # load the spacy model
    nlp = spacy.load(spacy_model) 
    # list all folders in the path
    dir = os.listdir(data_path) 

    # go through each folder
    for folder in tqdm(dir): #tqdm is a progress bar
        # get the path for the folder
        folder_path = os.path.join(data_path, f'{folder}') 
        # list all files in the path
        folder_dir = os.listdir(folder_path)
        # empty list to hold results
        folder_result = []

        # go though each file in the folder
        for file in tqdm(folder_dir): # tqdm is a progress bar
            # get the path for the file
            file_path = folder_path = os.path.join(data_path, f'{folder}', f'{file}') 

            # read the text
            with open(file_path, "r", encoding = "latin-1") as f:
                text = f.read()

            # cleaning
            text = re.sub('<.*?>', '', text) # removing everything inside < >
            text = re.sub('[\n\t]', ' ', text) # removing \n and \t

            # make into spaCy doc 
            doc = nlp(text)

            # get results for file
            result = nlp_counter(file, doc) # this is a function i made, see utils for more information
            folder_result.append(result) # append result of one file 

        # save folder df to csv
        folder_result_df = pd.DataFrame(folder_result, columns = ["Filename", "RelFreq NOUN", "RelFreq VERB", "RelFreq ADJ", "RelFreq ADV", "Unique PER", "Unique LOC", "Unique ORG"]) # make pandas df
        save_path = os.path.join("out", f'{folder}.csv') # path to save the csv
        folder_result_df.to_csv(save_path) # save the csv
    return None

def main():
    # get the arguments
    args = input_parse()
    # run the feature extraction
    feature_extraction(args.data_path, args.spacy_model)

if __name__ == "__main__": # if the script is run from the command line
    main() # run the main function