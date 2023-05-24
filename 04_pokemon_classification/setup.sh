# install venv (ucloud doesn't have it)
sudo apt-get update
sudo apt-get install python3-venv

# make a new env
python3.9 -m venv env/pokemon_env

# activate the enviroment for the assignment
source ./env/pokemon_env/bin/activate

# install packages
python3.9 -m pip install --upgrade pip # ucloud's version is old
python3.9 -m pip install -r requirements.txt

# download data
bash data/kaggle.sh

# prepare data
python3.9 src/prepare.py --test_val_split 0.7

# deactivate the env
deactivate