# Finetuned transformers from huggingface🤗
## Intro
This repository uses a neural network with the transformer architecture to find emotions in headlines. The transformer used in this repository is [Emotion English DistilRoBERTa-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) and is a finetuned version of [RoBERTa](https://huggingface.co/roberta-base), with the ability to classify emotions in text. The data is a collection of news articles, and are either actual news articles or fake articles. In this project only the headlines of the data is used. The data can be [found here](https://www.kaggle.com/datasets/jillanisofttech/fake-or-real-news) but is also available in this repository. 

## How to run
To run the code within this repository, you first have to setup a virtual environment containing all the necessary modules. I have provided a script that does this for you, and all you need on your computer beforehand is [pip](https://pypi.org/project/pip/) and [python](https://www.python.org/). The code was developed on ubuntu Debian GNU/Linux 11 (bullseye) with python 3.9.2 and pip 23.1.2. The computer did not have venv although it is a default part of python, so it is installed in setup.sh [line 2](https://github.com/AddiH/Cultural_Data_Science/blob/f5873508b625a63ccb3c6c93945588afaaed4965/Language/04_finetuned_transformers/setup.sh#L2) and [line 3](https://github.com/AddiH/Cultural_Data_Science/blob/f5873508b625a63ccb3c6c93945588afaaed4965/Language/04_finetuned_transformers/setup.sh#L3). Additionally pip is upgraded in [line 12](https://github.com/AddiH/Cultural_Data_Science/blob/f5873508b625a63ccb3c6c93945588afaaed4965/Language/04_finetuned_transformers/setup.sh#L12). Remember to modify this to suit your needs.

### Execute the code

In the terminal, navigate to this repository and run the following:
```
bash setup.sh
```
This installs the necessary modules in a virtual environment. Then, to produce the desired outputs, run the following code:
```
bash run.sh
```

## Output
The output of this repository can be found in results/ and contains three plots and three tables. 
This repository already contains the results of running the scripts. If you execute the script, the new output will simply overwrite the old output. 

## Repository structure
```
├── data
│   └── data.zip                    <- data in .zip format
├── results
│   ├── plots                       <- Folder containing plots
│   │   ├── complete.png      
│   │   ├── fake.png
│   │   └── real.png
│   ├── tables             
│   │   ├── complete.csv            <- Folder containing tables
│   │   ├── fake.csv
│   │   └── real.csv
├── src                      
│   └── emotion_extraction.py       <- Script extracting emotions
├── utils                     
│   └── fun.py.py                   <- Functions used in emotion_extraction.py
├── README.md
├── requirements.txt
├── run.sh                          <- Script that runs the analysis
├── setup.sh                        <- Script that unzips data and sets up the virtual environment
└── task_description.md             <- Original readme.md file, courtesy of Ross Deans Kristensen-McLachlan
```


###### This repository is part of a portfolio exam in [Language Analytics](https://kursuskatalog.au.dk/en/course/115693/Language-Analytics), which is one of the courses of the supplementary subject [Cultural Data Science at Aarhus University](https://bachelor.au.dk/en/supplementary-subject/culturaldatascience/). You can see an overview of all the projects I have completed for this subject [here](https://github.com/AddiH/Cultural_Data_Science). MIT licence applies. 
