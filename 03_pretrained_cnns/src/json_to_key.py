import os
import json
import pandas as pd

# get the path to the data directory
test = os.path.join('data','test_data.json')
train = os.path.join('data','train_data.json')
val = os.path.join('data','val_data.json')

# prepare lists
jsons = [test, train, val]
items = []

# read the json files and append the data to the list
for json_file in jsons:
    with open(json_file) as f:
        for line in f:
            item = json.loads(line)
            item_data = {
                'image_path': 'data/'+item['image_path'], # add the path to the image (add 'data/' to the beginning of the path)
                'class_label': item['class_label'], # get the class label
                'dataset': json_file.split('_')[0].split('/')[-1] # get the dataset name from the file name
            }
            items.append(item_data)

# create a dataframe from the list
df = pd.DataFrame(items)

# save the dataframe to a csv file
df.to_csv(os.path.join('data', 'key.csv'), index=False)