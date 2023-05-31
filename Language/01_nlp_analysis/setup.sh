# install venv (ucloud doesn't have it)
sudo apt-get update
sudo apt-get install python3-venv

# make a new env
python3 -m venv env/lang_ass_1_env

# activate the enviroment for the assignment
source ./env/lang_ass_1_env/bin/activate

# install packages
pip install --upgrade pip # ucloud version is outdated
python3.9 -m pip install -r requirements.txt
spacy download en_core_web_md # medium spaCy model 

# deactivate the env
deactivate