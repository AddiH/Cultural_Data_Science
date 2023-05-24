import os
import pandas as pd
import cv2
from tqdm import tqdm
import shutil
import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.vgg16 import (preprocess_input)
import numpy as np
from sklearn.metrics import classification_report


def delete_variants():
    '''
    Delete pokemon with underscore in the name from csv and directory, 
    as they are variants that look nearly identical to the original pokemon.
    '''
    # load the data
    pokemon = pd.read_csv(os.path.join('data', 'threeD', 'pokemon.csv'))
    # make a subset of pokemon with only the pokemon that have a underscore in the name
    pokemon_underscore = pokemon[pokemon['name'].str.contains('_')]
    # take the names and put them in a list
    delete_list = pokemon_underscore['name'].tolist()
    # add the path to the list
    delete_paths = [os.path.join('data', 'threeD', 'images', name + '.png') for name in delete_list]
    # delete the images
    for path in delete_paths:
        os.remove(path)
    # delete the pokemon from the dataframe
    pokemon = pokemon[~pokemon['name'].str.contains('_')] # ~ means not
    # overwrite the csv file
    pokemon.to_csv(os.path.join('data', 'threeD', 'pokemon.csv'), index=False)
    return None

def rename_pokemon():
    '''
    Rename the pokemon with special characters in their names.
    '''
    ## Flabebe
    # Encode the special characters
    flabebe = "Flab+\udcaeb+\udcae"

    # Construct the old and new file names
    flabebe_old_name = f"/work/pokemon/data/twoD/images/{flabebe}"
    flabebe_new_name = "/work/pokemon/data/twoD/images/Flabebe"

    # Rename the folder
    os.rename(flabebe_old_name, flabebe_new_name)

    ## Nidoran_m
    # Encode the special characters
    nidoran_m = "Nidoran\udcd4\udcd6\udce9"

    # Construct the old and new file names
    nidoran_m_old_name = f"/work/pokemon/data/twoD/images/{nidoran_m}"
    nidoran_m_new_name = "/work/pokemon/data/twoD/images/Nidoran-m"

    # Rename the folder
    os.rename(nidoran_m_old_name, nidoran_m_new_name)

    ## Nidoran_f
    # Encode the special characters
    nidoran_f = "Nidoran\udcd4\udcd6\udcc7"

    # Construct the old and new file names
    nidoran_f_old_name = f"/work/pokemon/data/twoD/images/{nidoran_f}"
    nidoran_f_new_name = "/work/pokemon/data/twoD/images/Nidoran-f"

    # Rename the folder
    os.rename(nidoran_f_old_name, nidoran_f_new_name)
    return None

def png_to_jpg(folder_path):
    '''
    Convert .png images to .jpg with white background.
    '''
    # get all the files in the folder
    dir = os.listdir(folder_path)

    # info message, as this can take a while
    print("[INFO] Converting images to jpg...")

    for file in tqdm(dir):
        # join the two strings in order to form the full filepath.
        src = os.path.join(folder_path, file)
        # load image with alpha channel. IMREAD_UNCHANGED to ensure loading of alpha channel
        image = cv2.imread(src, cv2.IMREAD_UNCHANGED)
        # make mask of where the transparent bits are
        trans_mask = image[:, :, 3] == 0
        # replace areas of transparency with white and not transparent
        image[trans_mask] = [255, 255, 255, 255]
        # new image without alpha channel...
        new_img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        # split path and filename
        folder_path, filename = os.path.split(src)
        # make first letter of filename uppercase
        filename = filename[0].upper() + filename[1:]
        # replace extension with .jpg
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        # save new image as jpg
        cv2.imwrite(os.path.join(folder_path, jpg_filename), new_img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        # delete old image
        os.remove(src)
    return None

def unique_removal():
    '''
    Use the rename_key.csv file to delete or rename images that are unique to either the 2D or 3D dataset.
    '''
    # read the csv file
    df = pd.read_csv(os.path.join('data', 'rename_key.csv'), delimiter = ';')

    for index, row in df.iterrows():
        # get the values from the row
        threeD = row['threeD'] 
        twoD = row['twoD']
        # get the paths
        threeD_path = os.path.join('data', 'threeD', 'images', threeD+'.jpg')
        twoD_path = os.path.join('data', 'twoD', 'images', twoD)

        if threeD == "not exist":
            # delete twoD
            shutil.rmtree(twoD_path)
        elif twoD == "not exist":
            # delete threeD
            os.remove(threeD_path)
        else:
            # rename twoD to be identical to threeD
            new_twoD_path = os.path.join('data', 'twoD', 'images', threeD)
            os.rename(twoD_path, new_twoD_path)
    return None

def move_images():
    '''
    Move all images from the threeD folder to the twoD folder.
    '''
    # move all pictures from threeD into appropriate folders in twoD
    threeD_dir = os.listdir(os.path.join('data','threeD','images'))

    # move threeD images to twoD
    for file in threeD_dir:
        # remove .jpg to get pokemon name
        pokemon_name = file[:-4]
        old_path = os.path.join('data','threeD','images',file)
        new_path = os.path.join('data','twoD','images', pokemon_name ,file)
        os.rename(old_path, new_path)

    # move images out to data/images
    old_path = os.path.join('data','twoD','images')
    new_path = os.path.join('data','images')
    os.rename(old_path, new_path)

    # move the key to data
    old_path = os.path.join('data','threeD','pokemon.csv')
    new_path = os.path.join('data','pokemon.csv')
    os.rename(old_path, new_path)

    # delete threeD images folder
    os.rmdir(os.path.join('data','threeD','images'))
    # delete threeD folder
    os.rmdir(os.path.join('data','threeD'))
    # delete twoD folder
    os.rmdir(os.path.join('data','twoD'))
    return None

def create_key():
    '''
    Create a key.csv file that contains the pokemon name, path to the image, the pokemon type and the pokemon generation.
    '''
    # read in pokemon.csv
    df = pd.read_csv(os.path.join('data', 'pokemon.csv'))
    # capitalise first letter the name
    df['name'] = df['name'].str.capitalize()

    # Function to list all files within a directory and its subdirectories
    def list_files(startpath):
        file_list = []
        for root, dirs, files in os.walk(startpath):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    # path to data
    dir_path = os.path.join('data', 'images')
    # get all file paths
    path = list_files(dir_path)
    # get the pokemon name from the file path
    name = [os.path.basename(os.path.dirname(file)) for file in path]

    # Create a pd df of pokemon names and their respective image paths
    key = pd.DataFrame({'name': name, 'path': path})

    # add a column to key with the type from the df
    key['type'] = key['name'].map(df.set_index('name')['type1'])
    # add generation
    key['generation'] = key['name'].map(df.set_index('name')['generation'])

    # save key as csv
    key.to_csv(os.path.join('data', 'key.csv'), index=False)

    # delete pokemon.csv
    os.remove(os.path.join('data', 'pokemon.csv'))
    return None

def split_key(train_frac):
    '''
    Split the key.csv file into train, validation and test sets.
    '''
    # read in key.csv
    key = pd.read_csv(os.path.join('data', 'key.csv'))

    # save a df with only generation 8 pokemon
    test = key[key['generation'] == 8]
    # save the df as a csv
    test.to_csv(os.path.join('data', 'test.csv'), index=False)

    # remove generation 8 pokemon from key
    key = key[key['generation'] != 8]

    # sample X% of the data
    train = key.sample(frac=train_frac, random_state=1)
    # save the df as a csv
    train.to_csv(os.path.join('data', 'train.csv'), index=False)

    # remove the X% of the data from key
    key = key.drop(train.index)

    # save the last X% as validation as csv
    val = key
    val.to_csv(os.path.join('data', 'val.csv'), index=False)

    # delete key.csv
    os.remove(os.path.join('data', 'key.csv'))
    return None

def mini_dataset(path, sample_size):
    '''
    Create a mini dataset with 10 images from each class.
    '''
    # load the dataframe
    df = pd.read_csv(path)

    # get the unique classes
    labels = df['type'].unique()

    # prepare a df to store the sampled images
    mini_dataset = pd.DataFrame()

    # loop over the classes and sample 10 images from each class
    for label in labels:
        # subset the dataframe to the class
        df_label = df[df['type'] == label]
        # sample 10 images
        df_sample = df_label.sample(sample_size)
        # append the sampled images to the mini_dataset dataframe
        mini_dataset = pd.concat([mini_dataset, df_sample])

    # save the mini_dataset dataframe to a csv file
    mini_dataset.to_csv(os.path.join('data','mini_' + os.path.basename(path)), index=False)
    return None

def data_flow(df_test, df_train, df_val, target_size, batch_size):
    '''
    Create a data generator for the train, validation and test sets.
    '''
    train_datagen = ImageDataGenerator(preprocessing_function = preprocess_input)

    train_images = train_datagen.flow_from_dataframe(
        dataframe = df_train,
        x_col = 'path',
        y_col = 'type',
        target_size = target_size,
        batch_size = batch_size,
        subset = 'training')

    val_datagen = ImageDataGenerator(preprocessing_function = preprocess_input)

    val_images = val_datagen.flow_from_dataframe(
        dataframe = df_val,
        x_col = 'path',
        y_col = 'type',
        target_size = target_size,
        batch_size = batch_size)

    test_datagen = ImageDataGenerator(preprocessing_function = preprocess_input)

    test_images = val_datagen.flow_from_dataframe(
        dataframe = df_test,
        x_col = 'path',
        y_col = 'type',
        target_size = target_size,
        batch_size = batch_size,
        shuffle = False)
    return test_images, train_images, val_images

def preds(model, test_images, train_images, df_test):
    '''
    Return y_test and pred.
    '''
    # Predict the label of the test_images
    pred = model.predict(test_images)
    pred = np.argmax(pred,axis=1)

    # Map the label
    labels = (train_images.class_indices)
    labels = dict((v,k) for k,v in labels.items())
    pred = [labels[k] for k in pred]
    y_test = list(df_test.type)
    return y_test, pred

def save_report(y_test, pred, save_path):
    '''
    Make and save the classification report to a txt file.
    '''
    # Predict the label of the test_images
    report = classification_report(y_test, pred)
    # Save the report   
    with open(save_path, 'w') as f:
        f.write(report)
    return None
