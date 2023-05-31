# make sure the kaggle.json (Access token for API from website) is in this folder.

# make new dir if not exist
mkdir -p ~/.kaggle 

# move token to dir
mv data/kaggle.json ~/.kaggle/kaggle.json

# download dataset
kaggle datasets download -d aashita/nyt-comments

# move to data folder
mv nyt-comments.zip data/

# unzip
unzip data/nyt-comments.zip -d data

# delete irrelevant files
rm data/ArticlesApril2017.csv  
rm data/ArticlesApril2018.csv  
rm data/ArticlesFeb2017.csv  
rm data/ArticlesFeb2018.csv  
rm data/ArticlesJan2017.csv  
rm data/ArticlesJan2018.csv  
rm data/ArticlesMarch2017.csv  
rm data/ArticlesMarch2018.csv  
rm data/ArticlesMay2017.csv  
