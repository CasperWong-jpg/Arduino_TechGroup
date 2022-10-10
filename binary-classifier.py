import os
import numpy as np 
import cv2 
import pickle 






#pre-processing states: 
# normalize image size, convert each image to arrays, balancing data-set 
def convert_img_toarray(path, label):   
    training_data = [] 
    for img in os.listdir(path): 
        image_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE) 

        #if resize, should do it here 

        training_data.append([image_array, label])


    return training_data 


def save_to_pckl(training_data): 
    pickle_out = open("Training.pickle", "wb") 
    pickle.dump(training_data, pickle_out)
    pickle_out.close() 


    
