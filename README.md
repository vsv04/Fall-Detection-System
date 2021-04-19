# Readily Implementable Fall Detection System for the Elderly using Thermal Image Segmentation and Convolutional Neural Networks

This GitHub repository hosts the programs, hardware list and the schematics for the fall detection system developed for a high school research project. This project is _**open-source**_ and anyone who is interested can download the instructions for assembling the system along with the Python code and put together a working fall detection system. This repository will be updated periodically as the system is further developed and refined. <br/>

The interested reader can read the [**Research Paper**](https://github.com/vsv04/Fall-Detection-System/tree/master/RESEARCH%20PAPER) that discusses the research goal, materials, methods and results. 

## Hardware
The [**Parts and Schematics**](https://github.com/vsv04/Fall-Detection-System/tree/master/PARTS%20%26%20SCHEMATICS) folder has a list of parts needed and assembly instructions for the fall detection system.<br/>

![](https://github.com/vsv04/Fall-Detection-System/blob/master/PARTS%20%26%20SCHEMATICS/Images/Fall_detection_system_V2.jpg)
![](https://github.com/vsv04/Fall-Detection-System/blob/master/PARTS%20%26%20SCHEMATICS/Images/Fall_detection_system_V3.jpg)<br/>
**Raspberry Pi 4 connected to the thermal camera and the final wall-mounted fall detection system**

## Software Libraries
The Deep Learning program uses Google's TensorFlow and Keras for Deep Learning and OpenCV for image processing. Follow the instructions available online for installing [**TensorFlow, Keras**](https://medium.com/@abhizcc/installing-latest-tensor-flow-and-keras-on-raspberry-pi-aac7dbf95f2) and [**OpenCV**](https://hackaday.io/project/7008-fly-wars-a-hackers-solution-to-world-hunger/log/23068-installing-opencv-on-a-raspberry-pi-the-easy-way) on the Raspberry Pi. Next, download and install [**pylepton**](https://github.com/groupgets/pylepton) which is a Python library for capturing images from the Lepton over SPI.  For sending alerts, install [**Twilio**](https://www.twilio.com/docs/libraries/python) API using the command **pip3 install twilio**.

## Python Programs
Download the Python programs in the [**CODE**](https://github.com/vsv04/Fall-Detection-System/tree/master/CODE) folder to a separate folder (e.g. '/home/pi/CODE') on the Raspberry Pi. The algorithm in the flowchart for training the neural network, shown below, was programmed in Python. Refer to [**CODE/Readme**](https://github.com/vsv04/Fall-Detection-System/blob/master/CODE/Readme.md) for instructions on how to use the programs. <br/>

![](https://github.com/vsv04/Fall-Detection-System/blob/master/CODE/Images/FlowchartSmall.jpg) <br/>
**Flowchart for training a neural network as applied to fall detection**
