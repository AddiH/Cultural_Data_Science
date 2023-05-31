import pandas as pd
import os
import sys
from tqdm import tqdm

sys.path.append(os.path.join('utils'))
from fun import *

def main():
    # print message for user
    print("[INFO] Extracting emotions...")

    # read in data
    df = pd.read_csv('data/fake_or_real_news.csv', usecols=['title', 'label'])

    # if you just want to test a little portion of the data:
    # df = df[:50]

    # add loading bar
    tqdm.pandas()

    # create a new column with the emotion of the title
    df['emotion'] = df['title'].progress_apply(classify_title)

    # create a bar plot and table of the emotions
    results(df, "Complete dataset", "complete")

    # create a bar plot and table of the emotions for the fake news
    fake_news = df[df['label'] == 'FAKE']
    results(fake_news, "Fake news", "fake")

    # create a bar plot and table of the emotions for the real news
    real_news = df[df['label'] == 'REAL']
    results(real_news, "Real news", "real")

if __name__ == "__main__":
    main()