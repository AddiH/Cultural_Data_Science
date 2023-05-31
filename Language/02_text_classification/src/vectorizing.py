import scipy.sparse as sp
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import argparse 

def input_parse():
    #initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--test_size",      type = float, default=0.2) # 80/20 train/test split
    parser.add_argument("--random_state",   type = int, default=69) # default random state
    parser.add_argument("--ngram_range", nargs='+', type=int, default=[1,2]) # default ngram range. Passed as a list of ints
    parser.add_argument("--max_df",         type = float, default=0.95) # default max df
    parser.add_argument("--min_df",         type = float, default=0.05) # default min df
    parser.add_argument("--max_features",   type = int, default=500) # default max features
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

def vectorizing(test_size, random_state, ngram_range, max_df, min_df, max_features):
    '''
    Function to vectorize data and split into train and test sets
    Also saves the parameters used in the same folder as data
    Read documentation for sklearn TfidfVectorizer and train_test_split for more information on parameters
    '''
    # changing ngram list to tuple
    ngram_range = tuple(ngram_range)
    # string with parameters
    string_parameters = f"Splitting with test_size = {test_size}, random_state = {random_state}. Vectorizing with ngram_range = {ngram_range}, max_df = {max_df}, min_df = {min_df}, max_features = {max_features}"
    # print parameters
    print(string_parameters)
    
    # read data
    data_path = os.path.join("in", "fake_or_real_news.csv")
    data = pd.read_csv(data_path, index_col=0)

    # split df
    # (this could be a problem with other data not labelled as "text" and "label")
    X = data["text"]
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = random_state) 

    # define vectorizer
    vectorizer = TfidfVectorizer(ngram_range = ngram_range, lowercase = True, max_df = max_df, min_df = min_df, max_features = max_features)       

    # fit vectorizer
    X_train_feats = vectorizer.fit_transform(X_train)   
    X_test_feats = vectorizer.transform(X_test) 

    # save data
    sp.save_npz(os.path.join("in", 'X_train_feats.npz'), X_train_feats)
    sp.save_npz(os.path.join("in", 'X_test_feats.npz'), X_test_feats)
    y_train.to_csv(os.path.join("in", 'y_train.csv'), index=False)
    y_test.to_csv(os.path.join("in", 'y_test.csv'), index=False)

    # save string
    with open(os.path.join("in", 'parameters.txt'), 'w') as f:
        f.write(string_parameters)

def main():
    # run input parse to get name
    args = input_parse()
    # pass args to function
    vectorizing(args.test_size, args.random_state, args.ngram_range, args.max_df, args.min_df, args.max_features)

# if this code is called from command line, run main
if __name__ == "__main__":
    main()