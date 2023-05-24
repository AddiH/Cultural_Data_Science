import sys
import os
import argparse
sys.path.append(os.path.join('utils'))
from homemade_functions import *

def input_parse():
    # initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument('--test_val_split', type=float, default=0.7)
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

def main(frac):
    # delete pokemon variants that are nearly identical to the original pokemon, to avoid an unbalanced dataset
    delete_variants()
    # rename pokemon with special characters in their names
    rename_pokemon()
    # convert png images with transparant background to jpg images with white background
    png_to_jpg(os.path.join('data', 'threeD', 'images'))
    # remove pokemon that are only present in one of the kaggle datasets
    unique_removal()
    # merge the two kaggle datasets
    move_images()
    # create an overview of all pokemon. Merge with kaggle csv resulting in a csv with pokemon name, type, generation, and image path
    create_key()
    # split the key into a train, test and validation set
    split_key(frac)

    # create a mini (testing) dataset with X images from each class
    mini_dataset(os.path.join('data', 'train.csv'), 5)
    mini_dataset(os.path.join('data', 'test.csv'), 1)
    mini_dataset(os.path.join('data', 'val.csv'), 3)

    return None

if __name__ == '__main__':
    args = input_parse()
    main(args.test_val_split)
