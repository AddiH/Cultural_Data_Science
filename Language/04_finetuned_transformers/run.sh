# activate virtual environment
source ./env/lang_ass_4_env/bin/activate

# run script
TF_CPP_MIN_LOG_LEVEL=2 python3 src/emotion_extraction.py

# deactive the venv
deactivate