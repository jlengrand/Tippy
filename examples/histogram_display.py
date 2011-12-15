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

The final output is an IplImage in this script.
To end the script, the user simply needs to hit a keyboard key with the input 
image in the foreground.

For now, only the grayscale function is available, but color images support 
should be added soon. 
'''

import cv
import tippy.statistics as st
import tippy.display_operations as do

hist = st.Histogram()

img_name = "tippy/data/gnu.jpg"
img = cv.LoadImage(img_name, cv.CV_LOAD_IMAGE_GRAYSCALE)
hist.compute_histogram(img)

hist_img = hist.hist2image() 

do.display_single_image(hist_img, "Gray-Level histogram of the gnu image")
