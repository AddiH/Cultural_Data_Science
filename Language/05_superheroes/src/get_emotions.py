import pandas as pd
from transformers import pipeline
import sys
from tqdm import tqdm
sys.path.append('utils')
from fun import clean_load, emotion
import os

def main():
    # load the data
    df = clean_load()

    # load the emotion model
    feelings = pipeline("text-classification", 
                            model="j-hartmann/emotion-english-distilroberta-base", 
                            top_k=7)

    # add loading bar
    tqdm.pandas()

    # apply emotion function to the history-text column, and save the 7 outputs in 7 new columns
    df[['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']] = df['history_text'].progress_apply(lambda x: pd.Series(emotion(x, feelings)))

    # save the dataframe to a csv file
    df.to_csv(os.path.join('data', 'emotions.csv'), index=False)

if __name__ == '__main__':
    main()