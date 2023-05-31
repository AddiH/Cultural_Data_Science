# activate virtual environment
source ./env/lang_ass_2_env/bin/activate

# run the code
#python3.9 src/vectorizing.py
python3.9 src/vectorizing.py --test_size 0.2 --random_state 42 --ngram_range 1 2 --max_df 0.95 --min_df 0.05 --max_features 500
python3.9 src/logistic_regression.py
#python3.9 src/neural_net.py
python3.9 src/neural_net.py --activation logistic --hidden_layer_sizes 30 20 --max_iter 1000 --random_state 42

# deactive the venv
deactivate