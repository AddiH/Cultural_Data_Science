# make sure the kaggle.json (Access token for API from website) is in this folder.

# make new dir
mkdir ~/.kaggle

# move token to dir
mv data/kaggle.json ~/.kaggle/kaggle.json

# download dataset
kaggle datasets download -d validmodel/indo-fashion-dataset

# move the dataset
mv indo-fashion-dataset.zip data/

# unzip
unzip data/indo-fashion-dataset.zip -d data/