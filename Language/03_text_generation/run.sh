folder_path="fast"

# activate virtual environment
source ./env/lang_ass_3_env/bin/activate

# preprocess data
TF_CPP_MIN_LOG_LEVEL=2 python3.9 src/preprocessing.py --testing_dataset yes --folder_path "$folder_path"
# HELP:
#python src/preprocessing.py --help

# train model
TF_CPP_MIN_LOG_LEVEL=2 python3.9 src/train.py --epochs 5 --batch_size 128 --folder_path "$folder_path"
# HELP:
#python src/train.py --help

# generate text
TF_CPP_MIN_LOG_LEVEL=2 python3.9 src/generate.py --prompt finally --length 10 --folder_path "$folder_path"
# HELP:
#python src/generate.py --help

# deactive the venv
deactivate