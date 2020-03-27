# Python Code for the Fall Detection System
This folder contains all the Python programs for the fall detection system. The user needs to create a folder **/home/pi/CODE/** on the Raspberry Pi and download all the programs to that folder.

## Pylepton
The [pylepton](https://github.com/vsv04/Fall-Detection-System/tree/master/CODE/pylepton) folder contains the python code for acquiring thermal images from the FLIR Lepton.

## Python code for saving thermal images
[Save_Images.py](https://github.com/vsv04/Fall-Detection-System/blob/master/CODE/Save_Images.py) allows the user to capture and save thermal images as jpg files. It is recommended that the user take about 40 images of a person standing or sitting in different parts of the room and about 20 images of a person lying on the floor as if someone had fallen.  If there is a bed in the room that the system should account for, take an additional 10 images of a person lying on the bed. Some sample images are shown below. After saving thermal images, sort them into the "Normal" and "Fallen" folders in "Training_Data".

![](https://github.com/vsv04/Fall-Detection-System/blob/master/CODE/Images/StandingSmall.jpg)
![](https://github.com/vsv04/Fall-Detection-System/blob/master/CODE/Images/FallenSmall.jpg)<br/>
**Thermal images of a person standing and lying on the floor (80x60 pixels)**

## Python code for training the neural network
[Train_Save_Network.py](https://github.com/vsv04/Fall-Detection-System/blob/master/CODE/Train_Save_Network.py) uses the saved images to train a convolutional neural network (CNN) and saves its defining information as "trained_model.h5". 

## Python code for real-time fall detection
[Real_Time.py](https://github.com/vsv04/Fall-Detection-System/blob/master/CODE/Real_Time.py) reads the saved CNN and runs the real time fall detection in a loop. The program captures and classifies images every 10 seconds but waits 60 seconds after a fall is detected and it calls for help. However, the code can be modified by the user. 
