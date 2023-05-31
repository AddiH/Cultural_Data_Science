# install venv (ucloud doesn't have it)
sudo apt-get update
sudo apt-get install python3-venv

# make a new env
python3 -m venv env/lang_ass_4_env

# activate the enviroment for the assignment
source ./env/lang_ass_4_env/bin/activate

# install packages
python3 -m pip install --upgrade pip # ucloud version is outdated
python3 -m pip install -r requirements.txt

# deactivate the env
deactivate

# unzip
unzip data/data.zip -d data/