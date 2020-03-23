#---------------------------------------------------------------------------
#                           Save_Image.py
#              Program to capture and save numbered JPG images
#                       Written By Vetri S Vel
#---------------------------------------------------------------------------
# Import libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from pylepton import Lepton
import tkinter as tk

#------------------------------------------------------
#                  VARIABLES
#------------------------------------------------------
#Save images to this location
directory = "/home/pi/FallDetection/Thermal Images"

#Starting image number
img_number = 1

#Color map for displaying images
CMAP = 'magma'

#------------------------------------------------------
#                  FUNCTIONS
#------------------------------------------------------
initialized = False
# Read images from FLIR Lepton 80x60 thermal camera
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

# Display images to monitor
def PlotImage(Im_mat):
    global initialized
    global ax1 #The plot has to be global
    
    if initialized == False:
        fig1, ax1 = plt.subplots(1,1)
        ax1.clear() #Clear the current plot
        ax1.set_xticks([]) #Get rid of ticks on the x and y axis
        ax1.set_yticks([])
        im1 = ax1.imshow(Im_mat, cmap=plt.get_cmap(CMAP), interpolation = 'none',vmin = 0, vmax = 256)
        
        initialized = True #Now it has been initialized
    else:
        #Use simple command
        ax1.imshow(Im_mat, cmap=plt.get_cmap(CMAP), interpolation = 'none',vmin = 0, vmax = 256)
   
    #Always show the new plot
    plt.show()

# Update the current image to be saved 
def update_im():
    global Im_mat #Im_mat needs to be a global variable because it will be used in the next two functions
    
    Im_mat = CaptureImage() #Retrieve the pixel values using another function
    
    #Display the new image
    PlotImage(Im_mat)
    
# Save images using img_number
def save_im():
    global Im_mat
    global img_number
    
    # Write image
    file_name = os.path.join(directory,str(img_number)+".jpg")
    print(file_name)
    cv2.imwrite(file_name, Im_mat)
    
    #Increment the file number
    img_number = img_number + 1
    
# Button function that calls update image and save image functions
def button_GUI():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    update = tk.Button(frame, 
                       text="Update", 
                       fg = "red",
                       command = update_im)
    update.pack(side=tk.LEFT)
    not_fallen = tk.Button(frame,
                       text="Save",
                       command = save_im)
    not_fallen.pack(side=tk.LEFT)

    root.mainloop()
    
#------------------------------------------------------
#                     MAIN CODE
#------------------------------------------------------
# Launch the GUI for taking and saving images
button_GUI()
    

