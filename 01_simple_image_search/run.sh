# activate virtual environment
source ./env/vis_ass_1_env/bin/activate

# run script
python src/top_chi.py --img image_0420.jpg

# example of running the code on another image within the flower folder:
# python src/top_chi.py --img image_0069.jpg

# example of running the code on another folder:
# python src/top_chi.py --img bulbasaur.jpg --img_folder data/pokemon

# deactivate venv
deactivate
