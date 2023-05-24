import pandas as pd
import os

# load the dataframe
df = pd.read_csv(os.path.join('data','key.csv'))

# get the unique classes
labels = df['class_label'].unique()

# get the unique datasets
datasets = df['dataset'].unique()

# prepare a df to store the sampled images
mini_dataset = pd.DataFrame()

for dataset in datasets:
    # subset the dataframe to the dataset
    df_subset = df[df['dataset'] == dataset]

    # loop over the classes and sample 10 images from each class
    for label in labels:
        # subset the dataframe to the class
        df_label = df_subset[df_subset['class_label'] == label]
        # sample 10 images
        df_sample = df_label.sample(10)
        # append the sampled images to the mini_dataset dataframe
        mini_dataset = pd.concat([mini_dataset, df_sample])

# save the mini_dataset dataframe to a csv file
mini_dataset.to_csv(os.path.join('data','mini_key.csv'), index=False)