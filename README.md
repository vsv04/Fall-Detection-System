# Real-time Fall Detection System for the Elderly Using Deep Learning and Thermal Imaging

This GitHub repository hosts the programs, hardware list and the schematics for the fall detection system developed for a high school research project. This project is _**open-source**_ and anyone who is interested can download the instructions for assembling the system along with the Python code and have a working fall detection system. 

The interested reader can download and read the [**Research Paper**](https://github.com/vsv04/Fall-Detection-System/blob/master/RESEARCH%20PAPER/Research%20Paper.pdf) (pdf document) which has all the details.


## Assembling the Fall Detection System
The [**Components List**](https://github.com/vsv04/Fall-Detection-System/tree/master/COMPONENTS%20LIST) folder has a list of parts needed for the fall detection system. Assembly instructions can be found in the [**Schematics**](https://github.com/vsv04/Fall-Detection-System/tree/master/SCHEMATICS) folder.

![](https://github.com/vsv04/Fall-Detection-System/blob/master/SCHEMATICS/Images/Fall_detection_system_V2.jpg)
![](https://github.com/vsv04/Fall-Detection-System/blob/master/SCHEMATICS/Images/Fall_detection_system_V3.jpg)
**Raspberry Pi 4 connected to the thermal camera and the fully assemled fall detection system**

## Downloading the Code
The Deep Learning program uses [Google's TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/). Instructions for installing TensorFlow and Keras on the Raspberry Pi can be found [here](https://keras.io/). 
The [**Code**](https://github.com/vsv04/Fall-Detection-System/tree/master/CODE) folder has the Python programs for the fall detection system. 

_**Install dependencies and prerequisites**_
```
sudo apt-get install python3-numpy
sudo apt-get install libblas-dev
sudo apt-get install liblapack-dev
sudo apt-get install python3-dev 
sudo apt-get install libatlas-base-dev
sudo apt-get install gfortran
sudo apt-get install python3-setuptools
sudo apt-get install python3-scipy
sudo apt-get update
sudo apt-get install python3-h5py
```

_**Then install TensorFlow and Keras**_
```
pip install scipy
pip install cython
pip install tensorflow
pip install keras
```
