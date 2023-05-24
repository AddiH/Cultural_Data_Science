# activate virtual environment
source ./env/pokemon_env/bin/activate


# A SIMPLE TEST, WITH A VERY LIMITED DATASET:

python src/train.py --testing_dataset yes
python src/plots.py --testing_dataset yes


# CUSTOMISING THE MODEL:

# python src/train.py --testing_dataset no --hidden_layers 2 --hidden_units_1 100 --hidden_units_2 30 --epochs 1 --batch_size 10 --initial_learning_rate 0.001 decay_steps 1000 --decay_rate 0.9 --target_size 244
# python src/plots.py --testing_dataset no --batch_size 10 --target_size 244 # must be identical to the batch size used in training


# HELP:
# python src/train.py -h

# deactive the venv
deactivate