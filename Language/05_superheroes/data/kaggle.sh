# make sure the kaggle.json (Access token for API from website) is in this folder.

# make new dir if not exist
mkdir -p ~/.kaggle 

# move token to dir
mv data/kaggle.json ~/.kaggle/kaggle.json

# download dataset
kaggle datasets download -d jonathanbesomi/superheroes-nlp-dataset

# move to data folder
mv superheroes-nlp-dataset.zip data/

# unzip
unzip data/superheroes-nlp-dataset.zip -d data
