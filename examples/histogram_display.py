'''
Created on Dec 15, 2011

@author: Julien Lengrand-Lambert
@email: julien@lengrand.fr
---
Here is a simple example of an histogram calculation on a grayscale image in 
Python.

The histogram calculation is performed using the OpenCV library. In order to
simplify the process, an Histogram class has been created, which contains all
necessary data for a proper output image creation.

The final output is a list of IplImages in this script. Each item is a graphical
representation of teh histogram result for one channel.

To end the script, the user simply needs to hit a keyboard key with the input 
image in the foreground. 
'''
import cv
import tippy.statistics as st
import tippy.display_operations as do

<<<<<<< HEAD
img_name = "tippy/data/tippy.jpg"
img = cv.LoadImage(img_name, cv.CV_LOAD_IMAGE_COLOR)
hist = st.Histogram(img)

imgs = hist.to_images() # list of Red, Green, Blue channels
do.display_single_image(imgs[2], "Blue channel histogram of the tippy image")
=======
img_name = "tippy/data/gnu.jpg"
img = cv.LoadImage(img_name, cv.CV_LOAD_IMAGE_COLOR)
hist = st.Histogram(img)

hist_img = hist.hist2image() 

do.display_single_image(hist_img[0], "Gray-Level histogram of the gnu image")
