import os
from tensorflow.keras.datasets import cifar10
import cv2
import numpy as np

def preprocess():
    '''
    Loads cifar10 dataset, splits into X and y for train and test data. 
    Then performs the following steps on X_train and X_test data: 
    1. transform all pictures to greyscale
    2. scales the pixels intensity down to fit within the range 0-1
    3. reshapes the data to 2D. (Thus row i contains all pixel intensities of picture i)
    The datasets are then saved in the "in" folder.
    '''

    # load data
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()

    # make all data greyscale with list comprehension
    X_train_grey = np.array([cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in X_train])
    X_test_grey = np.array([cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in X_test])

    # scale data
    X_train_scaled = (X_train_grey)/255.0
    X_test_scaled = (X_test_grey)/255.0

    # reshape data
    nsamples, nx, ny = X_train_scaled.shape
    X_train_dataset = X_train_scaled.reshape((nsamples,nx*ny))

    nsamples, nx, ny = X_test_scaled.shape
    X_test_dataset = X_test_scaled.reshape((nsamples,nx*ny))

    # save data
    np.save(os.path.join('in', 'X_train'), X_train_dataset)
    np.save(os.path.join('in', 'X_test'), X_test_dataset)
    np.save(os.path.join('in', 'y_train'), y_train)
    np.save(os.path.join('in', 'y_test'), y_test)

    return None

# main function
def main():
    preprocess()

# if this code is called from command line, run main
if __name__ == "__main__":
    main()