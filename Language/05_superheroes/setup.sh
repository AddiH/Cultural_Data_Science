# install venv (ucloud doesn't have it)
sudo apt-get update
sudo apt-get install python3-venv

# make a new env
python3 -m venv env/superheroes

# activate the enviroment for the assignment
source ./env/superheroes/bin/activate

# install packages
python3 -m pip install --upgrade pip # ucloud version is outdated
python3 -m pip install -r requirements.txt

# download data
bash data/kaggle.sh

# deactivate the env
deactivate