# Text classification
## Intro
This repository shows how a logistic regression and a neural network can be trained to predict whether a news story is real or fake. 
After you have run the code, you will find the trained models in models/ and classification reports in out/.

## How to run

To run the code within this repository, you first have to setup a virtual environment containing all the necessary modules. I have provided a script that does this for you, and all you need on your computer beforehand is [pip](https://pypi.org/project/pip/) and [python](https://www.python.org/). The code was developed on ubuntu Debian GNU/Linux 11 (bullseye) with python 3.9.2 and pip 23.1.2. The computer did not have venv although it is a default part of python, so it is installed in setup.sh [line 2](https://github.com/AddiH/Cultural_Data_Science/blob/9f2ce08494f4c0e82f9f51a3f6208d7c348ec50c/Language/02_text_classification/setup.sh#L2) and [line 3](https://github.com/AddiH/Cultural_Data_Science/blob/9f2ce08494f4c0e82f9f51a3f6208d7c348ec50c/Language/02_text_classification/setup.sh#L3). Additionally pip is upgraded in [line 12](https://github.com/AddiH/Cultural_Data_Science/blob/9f2ce08494f4c0e82f9f51a3f6208d7c348ec50c/Language/02_text_classification/setup.sh#L12). Remember to modify this to suit your needs.

### Execute the code

In the terminal, navigate to this repository and run the following:
```
bash setup.sh
```
then:
```
bash run.sh
```

## Repository structure
```
├── in
│   └── data.zip                  <- Compressed data
├── models                        <- Will contain models
│   └── ..
├── out                           <- Will contain results
│   └── ..
├── src
│   ├── logistic_regression.py    <- Script containing logistic regression
│   ├── neural_net.py             <- Script containing neural network
│   └── vectorizing.py            <- Vectorizing data
├── README.md                 
├── run.sh                        <- Script that runs the analysis
├── setup.sh                      <- Script that sets up the virtual environment
└── task_description.md           <- Original readme.md file, courtesy of Ross Deans Kristensen-McLachlan
```
## Customising the code
Wherever possible I have added the option to customise the models. See run.sh for examples.


###### This repository is part of a portfolio exam in [Language Analytics](https://kursuskatalog.au.dk/en/course/115693/Language-Analytics), which is one of the courses of the supplementary subject [Cultural Data Science at Aarhus University](https://bachelor.au.dk/en/supplementary-subject/culturaldatascience/). You can see an overview of all the projects I have completed for this subject [here](https://github.com/AddiH/Cultural_Data_Science). MIT licence applies. 
