'''
Contains all basic functions, such as image creation, copy, . . .
No Image processing complex algorithms here. 

Created on Nov 19, 2011

@author: Julien Lengrand-Lambert
@email: julien@lengrand.fr
'''

import sys
import cv

def create_same_image(in_img, zero=0):
    """
    Creates an image of same size, depth and number of channels as input image
    If zero is activated, the image content is set to 0 to avoid parasites.
    
    ---
    Ex:
    img = cv.LoadImage("../data/tippy.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE)
    copy_img = create_same_image(img, 0)
    """
    try :
        out_img = cv.CreateImage(cv.GetSize(in_img), 
                                 in_img.depth, 
                                 in_img.nChannels)
    except TypeError:
        raise TypeError("(%s) Image creation failed!" % (sys._getframe().f_code.co_name))

    if zero:
        cv.Zero(out_img)
        
    return out_img