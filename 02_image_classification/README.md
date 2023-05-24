# Simple image classification
## Intro
Within this repository you will find two machine learning algorithm that attempts to classify pictures from the [cifar-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset. One is a logistic regression classifier, while the other is a neural network classifier. The pre-processing steps are very simple:

1. transform pictures to greyscale
2. scale the pixels intensity down to fit within the range 0-1
3. reshape the data to 2D.

This flattened greyscale version of the image is then fed into the classifiers.

## How to run

To run the code within this repository, you first have to setup a virtual environment containing all the necessary modules. I have provided a script that does this for you, and all you need on your computer beforehand is [pip](https://pypi.org/project/pip/) and [python](https://www.python.org/). The code was developed on ubuntu Debian GNU/Linux 11 (bullseye) with python 3.9.2 and pip 23.1.2. The computer did not have venv although it is a default part of python, so it is installed in setup.sh [line 2](https://github.com/AU-CDS/assignment2-image-classification-AddiH/blob/e7788a70969436bb3bcf8ed9157f8f0b98b4a5f6/setup.sh#L2) and [line 3](https://github.com/AU-CDS/assignment2-image-classification-AddiH/blob/e7788a70969436bb3bcf8ed9157f8f0b98b4a5f6/setup.sh#L3). Additionally, pip is upgraded in [line 12](https://github.com/AU-CDS/assignment2-image-classification-AddiH/blob/e7788a70969436bb3bcf8ed9157f8f0b98b4a5f6/setup.sh#L12). Remember to modify this to suit your needs.

Clone the repository to your computer, and in the terminal navigate to this repository and run the following:
```
bash setup.sh
```
This pre-processes the data and installs the necessary modules in a virtual environment. Then, to train the models and produce the desired outputs, run the following code:
```
bash run.sh
```

## Repository structure
```
├── in
│   └── ..                    <- Will contain test and train data
├── models   
│   └── ..                    <- Will contain the models
├── out                       
│   └── ..                    <- Will contain reports on model performance 
├── src 
│   ├── log_reg.py            <- Script running the logistic regression and saving to /models and /out
│   ├── neural_net.py         <- Script running the neural net and saving to /models and /out
│   └── preprocess.py         <- Script executing the pre-processing script and saving output to /in
├── README.md                 
├── run.sh                    <- Script that runs all the scripts within the virtual environment
├── setup.sh                  <- Script that sets up the virtual environment and pre-processes data
└── task_description.md       <- Original readme.md file, courtesy of Ross Deans Kristensen-McLachlan
```

## Evaluation
Even though the parameters of these models have not been optimised, we can still have a look at the classification reports:

### Logistic regression:
```
              precision    recall  f1-score   support

           0       0.39      0.31      0.35      1000
           1       0.38      0.36      0.37      1000
           2       0.27      0.19      0.22      1000
           3       0.25      0.11      0.15      1000
           4       0.25      0.12      0.16      1000
           5       0.33      0.28      0.30      1000
           6       0.22      0.55      0.32      1000
           7       0.31      0.30      0.31      1000
           8       0.34      0.44      0.38      1000
           9       0.39      0.42      0.41      1000

    accuracy                           0.31     10000
   macro avg       0.31      0.31      0.30     10000
weighted avg       0.31      0.31      0.30     10000
```

### Neural net:
```
              precision    recall  f1-score   support

           0       0.28      0.23      0.25      1000
           1       0.39      0.24      0.30      1000
           2       0.25      0.27      0.26      1000
           3       0.24      0.08      0.12      1000
           4       0.23      0.22      0.22      1000
           5       0.26      0.37      0.30      1000
           6       0.26      0.15      0.19      1000
           7       0.30      0.31      0.30      1000
           8       0.27      0.54      0.36      1000
           9       0.40      0.46      0.43      1000

    accuracy                           0.29     10000
   macro avg       0.29      0.29      0.27     10000
weighted avg       0.29      0.29      0.27     10000
```
Usually it can be difficult to assess whether it is possible to tweak parameters to attain better scores, but in this instance, I can say for certain that it is possible to get better prediction results. As an example [this kaggle project](https://www.kaggle.com/code/kmldas/cifar10-resnet-90-accuracy-less-than-5-min) showcases a model that attains 90% accuracy, by applying a convolutional neural network. This is an incredible improvement from the ~30% accuracy achieved with the models in this repository. It is likely that the models presented here could be optimised even more, an exhaustive grid search is however beyond the scope of this project.

###### This repository is part of a portfolio exam in [Visual Analytics](https://kursuskatalog.au.dk/en/course/115695/Visual-Analytics), which is one of the courses of the supplementary subject [Cultural Data Science at Aarhus University](https://bachelor.au.dk/en/supplementary-subject/culturaldatascience/). You can see an overview of all the projects I have completed for this subject [here](https://github.com/AddiH/Cultural_Data_Science). MIT license applies. 
