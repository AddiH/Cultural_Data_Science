# install venv (ucloud doesn't have it)
sudo apt-get update
sudo apt-get install python3-venv

# make a new env
python3 -m venv env/vis_ass_1_env

# activate the enviroment for the assignment
source ./env/vis_ass_1_env/bin/activate

# install packages
python3.9 -m pip install --upgrade pip # ucloud version is outdated
python3.9 -m pip install -r requirements.txt

# deactivate the env
deactivate

# unzip the data
unzip data/flowers.zip -d data/flowers