# install venv (ucloud doesn't have it)
sudo apt-get update
sudo apt-get install python3-venv

# make a new env
python3 -m venv env/vis_ass_3_env

# activate the enviroment for the assignment
source ./env/vis_ass_3_env/bin/activate

# install packages
python3.9 -m pip install --upgrade pip # ucloud version is outdated
python3.9 -m pip install -r requirements.txt

# download data
bash data/kaggle.sh
# prepare the data
python3.9 src/json_to_key.py
# make mini_key
python3.9 src/mini_key.py

# deactivate the env
deactivate