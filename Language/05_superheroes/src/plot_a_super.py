import pandas as pd
import os
import sys
import argparse

sys.path.append(os.path.join('utils'))
from plot import hero_bar


def input_parse():
    # initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument('--name', type=str, default="Catwoman")
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

def main():
    # get name
    args = input_parse()
    # read the df
    df = pd.read_csv(os.path.join('data','emotions.csv'))
    # plot for hero
    hero_bar(args.name, df)

if __name__ == '__main__':
    main()