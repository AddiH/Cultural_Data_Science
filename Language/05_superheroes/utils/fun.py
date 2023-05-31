import os
import pandas as pd
from transformers import pipeline

def sentiment(text, function):
    '''
    Returns sentiment for input text. If the text is longer than 512 tokens, the text will be processed in chuncks of 512,
    and the result is the weighted sum of results from the chuncks. The function must be a transformers pipeline.
    '''
    weighted_positive_probs = 0 # holds result
    weighted_negative_probs = 0
    chunked_texts = [] # Initialize an empty list to hold the chunked texts
    chunk_size = 512 # Define the chunk size
    text_length = len(text) # Calculate the length of the text

    # generates a sequence of numbers starting from 0 and incrementing by chunk_size until it reaches text_length.
    for i in range(0, text_length, chunk_size): 
        chunk = text[i:i + chunk_size] # slice from i to i + chunk_size (first time it's 0:512, second time it's 512:1024, etc.) Can only take 512 values, so we want index 0 to (and including) 511.
        chunked_texts.append(chunk) # append the chunk to the list of chunked texts

    for chunk in chunked_texts: # for each chunck
        result = function(chunk) # get result from pipeline
        
        # Retrieve the most likely sentiment label and its corresponding score
        for item in result[0]:
            if item['label'] == 'NEGATIVE':
                negative_score = item['score']
            elif item['label'] == 'POSITIVE':
                positive_score = item['score']    
        #Calculate the weight based on the chunk length
        weight = len(chunk) / text_length

        # giving the scores weight based on proportion of total text
        weighted_positive_probs = weighted_positive_probs + (positive_score * weight)
        weighted_negative_probs = weighted_negative_probs + (negative_score * weight)

    return weighted_positive_probs, weighted_negative_probs


def emotion(text, function):
    '''
    Returns emotions for input text. If the text is longer than 512 tokens, the text will be processed in chuncks of 512,
    and the result is the weighted sum of results from the chuncks. The function must be a transformers pipeline.
    '''
    # holds results:
    anger = 0
    disgust = 0
    fear = 0
    joy = 0
    neutral = 0
    sadness = 0
    surprise = 0
    chunked_texts = [] 

    chunk_size = 512 # max length the model can take
    text_length = len(text) # length of input text

    # loop over the text, making chucks of size 512. Last chuck will be whatever is left 
    for i in range(0, text_length, chunk_size): 
        chunk = text[i:i + chunk_size]
        chunked_texts.append(chunk) 

    for chunk in chunked_texts: 
        result = function(chunk) # get result from pipeline
        weight = len(chunk) / text_length # the weight the chunck has on final result

        for item in result[0]:# get every score
            if item['label'] == 'anger':
                anger_score = item['score']
            elif item['label'] == 'disgust':
                disgust_score = item['score']
            elif item['label'] == 'fear':
                fear_score = item['score']
            elif item['label'] == 'joy':
                joy_score = item['score']
            elif item['label'] == 'neutral':
                neutral_score = item['score']
            elif item['label'] == 'sadness':
                sadness_score = item['score']
            elif item['label'] == 'surprise':
                surprise_score = item['score']
            
        # add the scores from the chunck to the results from the entire text
        anger = anger + (anger_score * weight)
        disgust = disgust + (disgust_score * weight)
        fear = fear + (fear_score * weight)
        joy = joy + (joy_score * weight)
        neutral = neutral + (neutral_score * weight)
        sadness = sadness + (sadness_score * weight)
        surprise = surprise + (surprise_score * weight)

    return anger, disgust, fear, joy, neutral, sadness, surprise

def clean_load():
    '''
    Loads the superhero dataset, and drops rows with a na value in columns "history text" or "gender" as data in these
    are needed for the analysis.
    '''
    # load the csv file
    df = pd.read_csv(os.path.join('data', 'superheroes_nlp_dataset.csv'))

    # remove row if it has nan in the history_text column 
    df = df.dropna(subset=['history_text'])
    # remove row if it has nan in the gender column
    df = df.dropna(subset=['gender'])

    # save the dataframe to a csv file
    df.to_csv(os.path.join('data', 'clean_superheroes_nlp_dataset.csv'), index=False)

    return df