import matplotlib.pyplot as plt 
import pandas as pd
import os
import numpy as np



def hero_bar(hero_name, df):
    '''
    Takes the name of a hero and the emotions.csv df and returns a barplot with the most likely emotions for that heros history_text
    '''
    # subset the dataframe to get the hero
    hero = df[df['name']==hero_name]

    # get the emotions columns from the hero dataframe
    hero_emotions = hero[['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']]

    # Transpose the df
    data_transposed = hero_emotions.T.reset_index()

    # Rename the columns
    data_transposed.columns = ['Emotion', 'Value']

    # Choose some pretty colors
    colors = plt.cm.Set2(range(7))

    # Plot the bar plot
    plt.bar(data_transposed['Emotion'], data_transposed['Value'], color=colors)
    plt.xlabel('Emotion')
    plt.ylabel('Value')
    plt.title(f'History of {hero_name}')
    # save the plot as a png file
    plt.savefig(os.path.join('plots', f'{hero_name}_barplot.png'))
    plt.clf()
    return None

def gender_mean_bar(gender, df):
    '''
    Returns a barplot with the mean value of emotions on a subset of df, based on gender.
    '''
    #Choose only heroes where the gender column is x
    heroes = df[df['gender'] == gender]

    # Get the emotions columns from the heroes dataframe
    hero_emotions = heroes[['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']]

    # Compute the mean values for each emotion
    mean_values = hero_emotions.mean()

    # Choose some pretty colors
    colors = plt.cm.Set2(range(7))

    # Plot the bar plot
    plt.bar(mean_values.index, mean_values.values, color=colors)
    plt.xlabel('Emotion')
    plt.ylabel('Mean Value')
    plt.title(f"Mean emotion probability of {gender.lower()} superheroes' backstory")
    # save the plot as a png file
    plt.savefig(os.path.join('plots', f'{gender}_barplot.png'))
    plt.clf()

def combined(df):
    '''
    Returns a barplot with female and male superheroes data next to each other.
    '''
    # Group the data by gender and calculate the mean values for each emotion
    gender_mean_values = df.groupby('gender')[['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']].mean()

    # Set the width of each bar
    bar_width = 0.35

    # Set the positions of the bars on the x-axis
    index = np.arange(len(gender_mean_values.columns))

    # Choose some pretty colors
    colors = plt.cm.Set2(range(len(gender_mean_values)))

    # Plot the bars for female and male
    plt.bar(index, gender_mean_values.loc['Female'], bar_width, color=colors[0], label='Female')
    plt.bar(index + bar_width, gender_mean_values.loc['Male'], bar_width, color=colors[1], label='Male')

    # Customize the x-axis labels
    plt.xlabel('Emotion')
    plt.ylabel('Mean Probability')
    plt.title("Mean emotion probability by gender")
    plt.xticks(index + bar_width/2, gender_mean_values.columns)

    # Add a legend
    plt.legend()
    # Save the plot as a png file
    plt.savefig(os.path.join('plots','Combined_barplot.png'))
    plt.clf()
