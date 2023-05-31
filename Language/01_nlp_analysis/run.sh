# activate virtual environment
source ./env/lang_ass_1_env/bin/activate

# run script
python src/get_features.py

# example of running the script with another path specified:
# python src/get_features.py --data_path folder_example/data

# example of running the script with another spacy model specified:
# python src/get_features.py --spacy_model en_core_web_sm

# deactivate venv
deactivate
