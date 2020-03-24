#-------------------------------------------------------------------------------------
#                            Train_Save_Network.py
# Preprocess Training Data then Train and Save the Convolutional Deep Learning Network
#                           Written By: Vetri S Vel
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#                 Import libraries
#-------------------------------------------------------------------------------------
import cv2
import numpy as np
import os
import keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.utils import to_categorical

#-------------------------------------------------------------------------------------
#                      Input Data
#-------------------------------------------------------------------------------------
# Specify the main folder, training data folder and categories
MainFolder = "/home/pi/CODE/"
TrainingDataset = "Training_Data"
ModelSaveFile = os.path.join(MainFolder,'trained_model.h5')

Categories = ["Fallen","Normal"]
# Create folder and file paths
TrainingPath = os.path.join(MainFolder,TrainingDataset)

# Specify the image resolution
Img_size_x = 80
Img_size_y  = 60

# Set deep learning parameters
DropoutParameter = 0.1           # To prevent overfitting
Epochs = 2                      # Number of times to cycle through images when training
NumConvFilters = 6               # Number of convolution filters for each layer
ConvFilterSize = (3,3)           # Size of convolution filters
Batch_Size = 1
Validation_Split = 0.0           # Fraction of images to set aside for testing accuracy

#-------------------------------------------------------------------------------------
#                    Initialize and read training data
#-------------------------------------------------------------------------------------

#Initialize training dataset
training_dataset=[]

# function to read image data and classification
for category in Categories:
    def preprocessing_data(folder_path):
        image_path=os.path.join(folder_path,category)
        for Image in os.listdir(image_path):
            img_file = os.path.join(image_path,Image)
            try:
                img_gray = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)/255.0
                training_dataset.append([img_gray,Categories.index(category)])
                print(img_file)
            except:
                print('Warning: Exception occured when reading/converting')
                print(img_file)
                pass
    
    preprocessing_data(TrainingPath)

# Extract images and labels from training dataset and store as separate arrays
ImageData = []
ClassificationData = []
for features, label in training_dataset:
    ImageData.append(features)
    ClassificationData.append(label)

# Resize image data for deep learning
ImageData = np.array(ImageData).reshape(-1, Img_size_x, Img_size_y ,1)

# Change type of classification data to 'int'
ClassificationData = np.array(ClassificationData).astype('int')

#-------------------------------------------------------------------------------------
#                          Shuffle training data
#-------------------------------------------------------------------------------------
def shuffle_in_unison(A, b):
    shuffled_A = np.empty(A.shape,dtype=A.dtype)
    shuffled_b = np.empty(b.shape,dtype=b.dtype)
    permutation = np.random.permutation(len(b))
    for old_index, new_index in enumerate(permutation):
        shuffled_A[new_index] = A[old_index]
        shuffled_b[new_index] = b[old_index]
    return shuffled_A, shuffled_b

ImageData, ClassificationData = shuffle_in_unison(ImageData, ClassificationData)

# print the shape of the image data array
print("Image data array size:")
print(ImageData.shape)

#-------------------------------------------------------------------------------------
#             Setup and Run Deep Learning Model
#-------------------------------------------------------------------------------------
# Convert classification data to categorial data
ClassificationData = to_categorical(ClassificationData)

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

# Run deep learning model to optimize weights and biases using training data
ModelFit = model.fit(ImageData, ClassificationData,
          batch_size=Batch_Size,
          epochs = Epochs,
          verbose=2,
          validation_split=Validation_Split)

#Save the model to a file
model.save_weights(ModelSaveFile)