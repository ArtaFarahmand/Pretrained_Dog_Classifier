#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Arta Farahmand    
# DATE CREATED:  May 4th, 2021                                
# REVISED DATE:  May 5th, 2021
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Grab the filename from folder specified as image_dir/
    in_files = listdir(image_dir)
    
    #print 10 items form the filenames from folder specified as image_dir/
    print("\nprint 10 filenames form image_dir")
    for idx in range(0, min(10, len(in_files)), 1):
        print("{:2d} file: {:>25}".format(idx + 1, in_files[idx]))
    
    # Empty dictionary name results_dic
    results_dic = dict()
    
    # Determining the number of items in the directory
    items_in_dic = len(results_dic)
    print("\n Empty Dictionary results_dic - n items=", items_in_dic)
    
    # Creating a new key-pair to dictionary ONLY when key doesn't already exist.
    # This dictionary's values is a list that contains only 1 item - the pet image label
    for idx in range(0, len(in_files), 1):
        # Skip files that start with . (ex. .DS_Store in Mac OSX)
        if in_files[idx][0] != ".":
            # Temp labels for the variables
            pet_label = ""
            pet_image = in_files[idx]
            low_pet_image = pet_image.lower()
            word_list_pet_image = low_pet_image.split("_")
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_label += word + " "
            pet_label = pet_label.strip()
            
            
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
            else:
                print("** Alert: key=", in_files[idx], "already exists in result_dic with value=", result_dic[in_files[idx]])
                
    # Iterate through the dictionary printing all keys and their associated values
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, "   pet label=", results_dic[key][0])
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
