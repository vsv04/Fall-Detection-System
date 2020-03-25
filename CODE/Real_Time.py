#-------------------------------------------------------------------------------------
#                                 Real_Time.py
# Preprocess Training Data then Train and Save the Convolutional Deep Learning Network
#                           Written By: Vetri S Vel
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#                              Import libraries
#-------------------------------------------------------------------------------------
import cv2
import numpy as np
import os
import tensorflow as tf
import time
import keras

import RPi.GPIO as GPIO
from twilio.rest import Client

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from keras.models import load_model
from pylepton import Lepton


#-------------------------------------------------------------------------------------
#                                Input Data
#-------------------------------------------------------------------------------------
# Specify the main folder, training data folder and categories
MainFolder = "/home/pi/CODE/"
TrainingDataset = "Training_Data"
ModelSaveFile = os.path.join(MainFolder,'trained_model.h5')
CaptureImage = "Capture.jpg"
CaptureFilename = os.path.join(MainFolder,CaptureImage)

Categories = ["Fallen","Normal"]
# Create folder and file paths
TrainingPath = os.path.join(MainFolder,TrainingDataset)

# Specify the image resolution
Img_size_x = 80
Img_size_y  = 60

DropoutParameter = 0.1           # To prevent overfitting
NumConvFilters = 6               # Number of convolution filters for each layer
ConvFilterSize = (3,3)           # Size of convolution filters

# Threshold for average fall score to exceed before calling for help
threshold = 0.7
# Number of previous fall scores that are average
NStack = 6
# Initialize array of fall scores
FallArray = np.zeros(NStack)

#Custom alert message sent when a fall is detected
alert_message = "Message from fall detection system: Grandma may have fallen. Please check on her."

#Information specific to your Twilio account
Twilio_SID = "**************************"
Twilio_Auth = "*******************"
Twilio_number = "+1**********"

#Phone number of person who will be notified if a fall is detected
alert_reciever_number = "+1**********"

Verbose = True
#-------------------------------------------------------------------------------------
#                                FUNCTIONS
#-------------------------------------------------------------------------------------

#the following line needs your Twilio Account SID and Auth Token
client = Client(Twilio_SID, Twilio_Auth)

def send_alert(alert_message):
    global client
    global Twilio_SID
    global Twilio_Auth
    global Twilio_number
    client.messages.create(to = alert_reciever_number, from_ = Twilio_number,
                       body=alert_message)

pins = [17,22,27] #Pins for R,G,B
#Set the mode to BCM (reference pins by BCM number)
GPIO.setmode(GPIO.BCM)
for n in pins: #Set up pins
    GPIO.setup(n,GPIO.OUT)
    
def LED(n):
    # 0 green  1 blue  2 red
    global pins
    GPIO.output(pins[0], n==2)
    GPIO.output(pins[1], n==1)
    GPIO.output(pins[2], n==0)
    
def CaptureImage():
    HPix = 80  # Image resolution in the the horizontal direction
    VPix = 60  # Image resolution in the the vertical direction
    
    # Code for capturing thermal image from FLIR Lepton sensor
    with Lepton() as l:
      a,_ = l.capture()
      
    # extend contrast
    cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
    
    # fit data into 8 bits
    np.right_shift(a, 8, a)
    
    # reshape data
    b = np.reshape(a,(VPix,HPix))
    return b

def ReadImage(filepath):
    Img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)/255.0  
    Img = Img.reshape(-1, Img_size_x, Img_size_y, 1)
    return Img

#-------------------------------------------------------------------------------------
#                          Setup Pretrained Model
#-------------------------------------------------------------------------------------
# Define the deep learning model
model = Sequential()
model.add(Conv2D(NumConvFilters, ConvFilterSize, input_shape=(Img_size_x,Img_size_y ,1)))
model.add(Activation('relu'))
model.add(Dropout(DropoutParameter))

model.add(Flatten())  

model.add(Dense(2))
model.add(Activation('softmax'))

# Coompile the deep learning model
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


model.load_weights(ModelSaveFile)

#-------------------------------------------------------------------------------------
#                          Setup Pretrained Model
#-------------------------------------------------------------------------------------

while True:
    while True:
        # Capture thermal image
        LED(1) # Blue
        Img_mat= CaptureImage()
        cv2.imwrite(CaptureFilename, Img_mat)
        Img = ReadImage(CaptureFilename)
        LED(0) # Green
        
        Prediction = model.predict(Img)
        FallScore = Prediction[0][0]
        
        if Verbose: print("Fall Score: " + str(FallScore))
        
        FallArray[:-1] = FallArray[1:];
        FallArray[-1] = FallScore;
        
        #Check whether to call for help
        if np.mean(FallArray) > threshold:
            #Break out of the normal loop and call for help
            break
        
        time.sleep(10)
        
    #Call for help
    send_alert(alert_message)
    
    LED(2) # Red
    
    if Verbose: print("Called for help")
    
    #Delay before resuming normal loop
    time.sleep(60)
