import os
import numpy as np 
import cv2 
import pickle 
import tensorflow as tf 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers   import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D 



#pre-processing states: 
# normalize image size, convert each image to arrays, balancing data-set 
def convert_img_toarray(path, label):   
    training_data = [] 
    for img in os.listdir(path): 
        image_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE) 

        #if resize, should do it here 

        training_data.append([image_array, label])


    return training_data 


def save_to_pckl(training_data, name): 
    pickle_out = open(name, "wb") 
    pickle.dump(training_data, pickle_out)
    pickle_out.close() 


def load_data(x_path, y_path): 
    X = pickle.load(open(x_path, "rb")) 
    y = pickle.load(open(y_path, "rb"))

    return (X,y) 


def add_set_of_layers(model, X, input_shape): 

    if input_shape: 
        first_sub_layer = Conv2D(64, (3,3), input_shape = X.shape[1:] ) 
    else: 
        first_sub_layer = Conv2D(64, (3,3)) 

    model.add(first_sub_layer)
    second_sub_layer = Activation("relu") 
    model.add(second_sub_layer)
    third_sub_layer = MaxPooling2D(pool_size=(2,2))
    model.add(third_sub_layer)


def add_output_layers(model): 
    model.add(Dense(1)) 
    model.add(Activation("sigmoid")) 


def model_and_train(X, y, batch_size): 
    model = Sequential() 

    #first layer 
    add_set_of_layers(model, X, input_shape = True) 

    #second layer
    add_set_of_layers(model, X, input_shape=False) 

    #third layer 
    model.add(Flatten()) 
    model.add(Dense(64)) 

    #output layer 
    add_output_layers(model) 


    #train
    model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ["accuracy"])
    model.fit(X, y, batch_size, validation_split = 0.1)

    
