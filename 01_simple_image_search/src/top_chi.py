import os
import sys
import pandas as pd
from tqdm import tqdm
import cv2
import argparse 

def input_parse():
    #initialise parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--img", type = str, required=True) # must specify which photo to compare with (e.g. "img_0001.jpg")
    parser.add_argument("--img_folder", type = str, default=os.path.join("data", "flowers")) # default flower folder
    # parse the arguments from command line
    args = parser.parse_args()
    # get the variables
    return args

def top_chi(img, img_folder):    
    '''
    Takes an image and finds the 5 images with the most similar (least chi) color histogram. 
    Saves filename and chi of the top 5 imgages in a pandas df in the out_folder.
    Saves the original and top 5 images to the out_folder
    
    img = original image to find matches to
    img_folder = path to folder with all images
    '''
    out_folder = os.path.join("out", f"best_match_to_{img[:-4]}") # the subfolder for results
    if not os.path.exists(out_folder): # make it if it doesn't exist
        os.mkdir(out_folder)
    
    # load og img and get relevant data on it
    og_path = os.path.join(img_folder, img) # path to og image
    og_img = cv2.imread(og_path) # read in og image
    og_img_save_path = os.path.join(out_folder, f'original_{img}') # save path for og_img
    cv2.imwrite(og_img_save_path, og_img) # save pic
    og_hist = cv2.calcHist([og_img], [0,1,2], None, [256,256,256], [0,256, 0,256, 0,256]) # histogram of og img
    og_hist_norm = cv2.normalize(og_hist, og_hist, 0, 1.0, cv2.NORM_MINMAX) # normalised histogram
    
    # loop over all pics to find the most similar
    results = [] # empty list to hold results
    for file in tqdm(os.listdir(img_folder)): # for all files in folder - with a loading bar
        compare_img_path = os.path.join(img_folder, file) # path to first img
        compare_img = cv2.imread(compare_img_path) # read in img
        compare_hist = cv2.calcHist([compare_img], [0,1,2], None, [256,256,256], [0,256, 0,256, 0,256]) # histogram
        compare_hist_norm = cv2.normalize(compare_hist, compare_hist, 0, 1.0, cv2.NORM_MINMAX) # normalised histogram
        chi = round(cv2.compareHist(og_hist_norm, compare_hist_norm, cv2.HISTCMP_CHISQR), 2) # chi result of comparison
        results.append((file, chi)) # save results

    # save the results in a df
    comparison_results_df = pd.DataFrame(results, columns = ["file", "chi"]) # make results into pd df
    df_without_original = comparison_results_df[comparison_results_df['chi'] != 0] # remove chi = 0, aka identical pics
    sorted = df_without_original.sort_values(by=['chi']) # sort by chi
    best_fit = sorted.iloc[0:5, ] # slice the first 5 rows

    save_path = os.path.join(out_folder, f"best_match_to_{img[:-4]}.csv") # make savepath without the .jpg (note the [:-4])
    best_fit.to_csv(save_path, index=False) # save the pd df in csv

    # save the most similar pics from the pd df
    for row in best_fit.itertuples(index=False): # loop over all rows
        compare_img_path = os.path.join(img_folder, row.file) # make path to img
        compare_img = cv2.imread(compare_img_path) # load img
        img_save_path = os.path.join(out_folder, row.file) # make save path
        cv2.imwrite(img_save_path, compare_img) # save img

def main():
    # run input parse to get name
    args = input_parse()
    # pass args to function
    top_chi(args.img, args.img_folder)

# if this code is called from command line, run main
if __name__ == "__main__":
    main()