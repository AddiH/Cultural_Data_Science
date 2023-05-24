import sys
import os
import pandas as pd
import argparse
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from tensorflow.keras.models import load_model

sys.path.append(os.path.join('utils'))
from homemade_functions import preds, save_report, data_flow
from plotting import count_types, plot_cm

def input_parse():
    # initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument('--testing_dataset', type=str, default="no", choices=["yes", "no"],
                        help="Specify whether to use a subset of the data for testing the code. (Options: yes, no)")
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--target_size', type=int, default=244)
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args




def main(testing_dataset, batch_size, target_size):
    # load the model
    model = load_model(os.path.join('results', 'model'))
    
    # load fullsize or minisize dataset
    if testing_dataset == "no":
        df_train = pd.read_csv(os.path.join('data', 'train.csv'))
        df_test = pd.read_csv(os.path.join('data', 'test.csv'))
        df_val = pd.read_csv(os.path.join('data', 'val.csv'))
    elif testing_dataset == "yes":
        df_train = pd.read_csv(os.path.join('data', 'mini_train.csv'))
        df_test = pd.read_csv(os.path.join('data', 'mini_test.csv'))
        df_val = pd.read_csv(os.path.join('data', 'mini_val.csv'))
    
    # combine all data
    df = pd.concat([df_train, df_test, df_val])
    
    # use the name of pokemon to filter the dataframe, saving only unique pokemon
    unique = df.drop_duplicates(subset=['name'])

    # delete:
    print(len(df)) # 3272
    print(len(unique)) #876
    # print the lengt of df where generation == 8
    print(len(unique[unique['generation'] == 8])) # 85

    
    # plot the number of pokemon per type
    save_path = os.path.join('results', 'plots', 'unique_pokemon_type.png')
    count_types(unique, None, save_path)
    
    target_size = (target_size, target_size)

    # prepare the data
    test_images, train_images, val_images = data_flow(
    df_test, df_train, df_val, target_size, batch_size)
    # get predictions
    y_test, pred = preds(model, test_images, train_images, df_test)
    
    # plot the confusion matrix
    save_path = os.path.join('results', 'plots', 'confusion_matrix.png')
    plot_cm(y_test, pred, save_path, normalized=False)
    
    # save the report
    save_report(y_test, pred, os.path.join('results', 'report.txt'))

if __name__ == "__main__":
    args = input_parse()
    main(args.testing_dataset, args.batch_size, args.target_size)
