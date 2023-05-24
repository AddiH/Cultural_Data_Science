# activate the enviroment for the assignment
source ./env/vis_ass_3_env/bin/activate

# run the training
python src/train.py --testing_dataset yes

# an example of running another model with the entire dataset:
# python src/train.py -- testing_dataset no --hidden_layers 2 --hidden_units 20 --epochs 5 --batch_size 40 --target_size 200 --initial_learning_rate 0.03 --decay_steps 500 --decay_rate 0.8

# deactivate the env
deactivate


