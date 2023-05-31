from matplotlib import pyplot as plt
import pandas as pd
import os
from transformers import pipeline
import tensorflow
import logging

# Set the logging level for transformers library
logging.getLogger("transformers").setLevel(logging.ERROR)

def classify_title(title):
    # Load the classifier pipeline
    classifier = pipeline("text-classification", 
                        model="j-hartmann/emotion-english-distilroberta-base", 
                        top_k=1) # show only the label with the highest probability
    # Apply the classifier to the title and return the label
    result = classifier(title)
    return result[0][0]['label']  # Extract the label from the result

def results(data, title, save_name):
    # get counts
    counts = data['emotion'].value_counts()

    # make sure the emotions are in the right order
    counts = counts.reindex(['neutral', 'fear', 'disgust', 'sadness', 'joy', 'anger'])

    # Make a df with the emotions and their counts
    table = pd.DataFrame({'emotion': counts.index, 'count': counts.values})

    # Save the df to a csv file
    save_path = os.path.join('results', 'tables', save_name)
    table.to_csv(save_path)

    # Choose some pretty colors
    colors = plt.cm.Set2(range(len(counts)))

    # Create a bar plot
    plt.bar(table['emotion'], table['count'], color=colors)
    #plt.bar(counts.index, counts.values, color=colors)

    # Set the plot labels and title
    plt.xlabel('Emotion')
    plt.ylabel('Count')
    plt.title(title)

    # Save the plot
    save_path = os.path.join('results', 'plots', save_name + '.png')
    plt.savefig(save_path)
    plt.close()
    return None
