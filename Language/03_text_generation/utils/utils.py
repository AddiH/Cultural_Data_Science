import numpy as np
import pandas as pd
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow.keras.utils as ku
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Embedding, LSTM


def get_sequence_of_tokens(tokenizer, corpus):
    '''
    This function takes in the tokenizer and corpus and returns input sequences.
    Words turned into tokens and turned into n_grams sequences.
    '''
    input_sequences = []
    # iterate through the corpus
    for comment in corpus:
        # turn words into tokens
        token_list = tokenizer.texts_to_sequences([comment])[0]
        # iterate through the tokens
        for i in range(1, len(token_list)):
            # take the first two tokens and append. Then the first three tokens and append, etc.
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)
    return input_sequences

## pad predictor sequences and convert labels to one-hot encoding
def generate_padded_sequences(input_sequences, total_unique_words):
    '''
    Pads the input sequences to the max sequence length.
    Extracts and converts labels to one-hot encoding.
    '''
    # get max sequence length (longest comment)
    max_sequence_len = max([len(x) for x in input_sequences])
    # pad the input sequences
    input_sequences = np.array(pad_sequences(input_sequences, 
                                            maxlen = max_sequence_len, 
                                            padding = 'pre')) 
    # split off the last word as the label
    predictors, label = input_sequences[:,:-1], input_sequences[:,-1]
    # convert labels to one-hot encoding
    label = ku.to_categorical(label, 
                            num_classes = total_unique_words) 
    return predictors, label, max_sequence_len

def create_model(max_sequence_len, total_unique_words):
    '''
    Creates the model.
    '''
    input_len = max_sequence_len - 1
    model = Sequential()
    
    # Add Input Embedding Layer
    model.add(Embedding(total_unique_words,  
                        10,  
                        input_length = input_len)) 
    
    # Add Hidden Layer 1 - LSTM Layer
    model.add(LSTM(100)) 
    model.add(Dropout(0.1)) 
    
    # Add Output Layer
    model.add(Dense(total_unique_words, 
                    activation='softmax')) 

    # Compile the model
    model.compile(loss='categorical_crossentropy', 
                    optimizer='adam') 
    return model


def generate_text(seed_text, next_words, model, max_sequence_len, tokenizer):
    '''
    Generates text based on a prompt and the model.
    '''
    # iterate through the number of words to generate
    for _ in range(next_words): 
        # turn the seed text into tokens
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        # pad the tokens
        token_list = pad_sequences([token_list], 
                                    maxlen=max_sequence_len-1, 
                                    padding='pre') 
        # predict the next word
        predicted = np.argmax(model.predict(token_list), 
                                            axis=1) 
        
        output_word = "" 
        # iterate through the tokenizer to find the word that matches the predicted token
        for word, index in tokenizer.word_index.items(): 
            # if the index matches the predicted token
            if index == predicted: 
                output_word = word
                break # break out of the loop
        # add the predicted word to the seed text    
        seed_text += " "+output_word 
    return seed_text.capitalize() 