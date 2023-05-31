# NLP analysis of The Uppsala Student English Corpus
## Intro
The purpose of this repository is to analyse texts from The Uppsala Student English (USE) Corpus using the python module spaCy. The code available here calculates the relative frequency of nouns, verbs, adjective, and adverbs per 10,000 words for each document using the part-of-speech tagging available within spaCy. Additionally, the programme coded here finds the total number of unique PER, LOC and ORGS in each text. PER, LOC, ORGS are variables in spaCy’s named entity recognition, and refers to person, location and organization. The original prompt for this assignment is available in the file [task_description.md](task_description.md). You can also find additional information on [spaCy](https://spacy.io/) and the [USEcorpus](in/readme.md).

## How to run

To run the code within this repository, you first have to setup a virtual environment containing all the necessary modules. I have provided a script that does this for you, and all you need on your computer beforehand is [pip](https://pypi.org/project/pip/) and [python](https://www.python.org/). The code was developed on ubuntu Debian GNU/Linux 11 (bullseye) with python 3.9.2 and pip 23.1.2. The computer did not have venv although it is a default part of python, so it is installed in setup.sh [line 2](https://github.com/AddiH/Cultural_Data_Science/blob/5f0b7e177a73a584c6b7acf8e07b0853f1b3dbf1/Language/01_nlp_analysis/setup.sh#L2) and [line 3](https://github.com/AddiH/Cultural_Data_Science/blob/5f0b7e177a73a584c6b7acf8e07b0853f1b3dbf1/Language/01_nlp_analysis/setup.sh#L3). Additionally pip is upgraded in [line 12](https://github.com/AddiH/Cultural_Data_Science/blob/5f0b7e177a73a584c6b7acf8e07b0853f1b3dbf1/Language/01_nlp_analysis/setup.sh#L12). Remember to modify this to suit your needs.

### Execute the code

In the terminal, navigate to this repository and run the following:
```
bash setup.sh
```
then:
```
bash run.sh
```

## Output
The data is organised into 14 different folders, and the output is organised accordingly. For each folder a table with the following structure is produced:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|

This repository already contains the results of running the scripts. If you execute the script, the new output will simply overwrite the old output. 

## Repository structure
```
├── in
│   ├── USEcorpus             
│   │   ├── a1                <- Subfolder with a subset of text
│   │   │   ├── 0100.a1.txt   <- One text file
│   │   │   ├── 0101.a1.txt
│   │   │   └── ..
│   │   ├── a2
│   │   └── ..
│   └── readme.md             <- Details on the USEcorpus, courtesy of Ross Deans Kristensen-McLachlan
├── out                       
│   ├── a1.csv                <- Results for all texts in one folder
│   ├── a2.csv
│   └── ..
├── src                      
│   └── get_features.py       <- Script looping over all folders and extracting information
├── utils                     
│   └── nlp_counter.py        <- Function counting part-of-speech and named-entity-recognition
├── README.md                 
├── run.sh                    <- Script that runs the analysis
├── setup.sh                  <- Script that sets up the virtual environment
└── task_description.md       <- Original readme.md file, courtesy of Ross Deans Kristensen-McLachlan
```
## Customising the code
If you wish to run the code on different data or use another spaCy model, you can adjust the code:

To run the code on different data, do the following:
-	Ensure the data is in the correct format, that means it is contained in a folder with subfolders, and the files are all of the .txt. format.
-	Pay attention to the encoding in line 48 in the [get_features.py](src/get_features.py) script. Your data might have other encoding than “latin-1”
-	Pay attention to the “cleaning” step in line 52-53 in the [get_features.py](src/get_features.py) script. You might require different pre-processing.
-	Modify the [run.sh](run.sh) script to include the correct path to your data. You will find an example of how to do this in line 8.

To use a different spacy model, do the following:
-	Add the desired model to the environment by adding it in the [setup.sh](setup.sh) file.
-	Modify the [run.sh](run.sh) script so it specifies the desired model. Again, an example is available in line 11.


###### This repository is part of a portfolio exam in [Language Analytics](https://kursuskatalog.au.dk/en/course/115693/Language-Analytics), which is one of the courses of the supplementary subject [Cultural Data Science at Aarhus University](https://bachelor.au.dk/en/supplementary-subject/culturaldatascience/). You can see an overview of all the projects I have completed for this subject [here](https://github.com/AddiH/Cultural_Data_Science). MIT licence applies. 
