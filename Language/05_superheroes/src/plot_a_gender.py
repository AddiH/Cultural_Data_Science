import pandas as pd
import os
import sys

sys.path.append(os.path.join('utils'))
from plot import gender_mean_bar, combined

def main():
    # read the df
    df = pd.read_csv(os.path.join('data','emotions.csv'))

    # get the individual plots
    gender_mean_bar("Female", df)
    gender_mean_bar("Male", df)

    # plot a combined plot
    combined(df)

if __name__ == '__main__':
    main()