# Text generation with recurrent neural network
## Intro
This repository shows how a recurrent neural network (RNN) can be used to generate text. A RNN is a specific type of neural network designed to process sequential data by preserving and utilising information from previous steps. The architecture of an RNN contain loops that allows the network to retain and propagate information across time. After the RNN has trained on a dataset, it can generate text from a prompt, by predicting the most likely word to follow. 
Using tools from tensorflow, a RNN is trained on comments from the New York Times website. The comments are from [this kaggle dataset](https://www.kaggle.com/datasets/aashita/nyt-comments) and contains data from Jan-May 2017 and Jan-April 2018.


## How to run

To run the code within this repository, you first have to setup a virtual environment containing all the necessary modules. I have provided a script that does this for you, and all you need on your computer beforehand is [pip](https://pypi.org/project/pip/) and [python](https://www.python.org/). The code was developed on ubuntu Debian GNU/Linux 11 (bullseye) with python 3.9.2 and pip 23.1.2. The computer did not have venv although it is a default part of python, so it is installed in setup.sh [line 2]() and [line 3](). Additionally pip is upgraded in [line 12](). Remember to modify this to suit your needs.

### Get kaggle dataset
This code downloads data through the kaggle API. You need to sign up to [kaggle.com](https://www.kaggle.com/) and though your account, download your personal token - a json file. If you are unsure of how to do this, you can read kaggle's description below:

*"From the site header, click on your user profile picture, then on “My Account” from the dropdown menu. This will take you to your account settings at https://www.kaggle.com/account. Scroll down to the section of the page labelled API. To create a new token, click on the “Create New API Token” button. This will download a fresh authentication token onto your machine."*

**Move the token into the data folder** - then you're ready to run the code:

### Execute the code

In the terminal, navigate to this repository and run the following:
```
bash setup.sh
```
This downloads the data, installs the necessary modules in a virtual environment and trains the model. Then, to generate text run:
```
bash generate.sh
```
Note: As a default the run.sh script uses a tiny version of the dataset, so it is possible to test whether the code works, without waiting for a large dataset to be processed. See how to change this in the "customising" part of this readme.

## Output
The trained model will be in model/ and the output from the text generation will be printed to the terminal when you run the script.

## Repository structure
```
  ├── data          
  │   └── kaggle.sh                  <- Bash script downloading the datasets
  ├── in                             <- Will hold the preprocessed dataset
  │   └── ..          
  ├── models                         <- Will hold your trained model
  │   └── ..          
  ├── src          
  │   ├── generate.py                <- Script generating new text from trained model
  │   ├── preprocessing.py           <- Script executing one hot encoding, padding etc
  │   └── train.py                   <- Script training and saving the model
  ├── utils          
  │   └── utils.py                   <- Functions - primarily for preprocessing
  ├── LICENSE          
  ├── README.md          
  ├── requirements.txt               <- .txt containing needed modules and versions
* ├── run.sh                         <- Script that executes preprocessing.py, train.py and generate.py
  ├── setup.sh                       <- Script that sets up the virtual environment and downloads data
  └── task_description.md            <- Assignment prompt by Ross Deans Kristensen-McLachlan
  
* files that you can change if you wish to customise the code.
```

# Customising

The run.sh has a couple options for customisation. 
- The very first line defines the name of the folders the results will be saved to. That way you can try out different models. Simply change the string to something else, and your data, tokenizer and model will be saved to subfolders with this name. 
- Below each line executing a script, you will find a line of code that will display helpful text explaining the flags of a script. Play around with these to make another model or preproces the data in another way.
- If you've already trained a model and just want to generate text, you can just comment out line 7 and 12 - they run the preprocessing and train script

Remember: you only need to run setup.sh once, but you can execute run.sh as many times as you wish, customising the code to find the funniest output.

## Evaluation
I've only run this code on computers with poor processing power, resulting in very bad generated text. Usually this means an output that starts with the prompted word, followed by "the" repeated until the end of the sentence. If this happens to you, you should modify the code to ensure you are running the scripts on the full dataset, with appropriate model parameters. The model will take a while to train, so be patient :)

###### This repository is part of a portfolio exam in [Language Analytics](https://kursuskatalog.au.dk/en/course/115693/Language-Analytics), which is one of the courses of the supplementary subject [Cultural Data Science at Aarhus University](https://bachelor.au.dk/en/supplementary-subject/culturaldatascience/). You can see an overview of all the projects I have completed for this subject [here](https://github.com/AddiH/Cultural_Data_Science). MIT license applies. 
