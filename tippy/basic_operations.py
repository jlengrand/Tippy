'''
Contains all basic functions, such as image creation, copy, . . .
No Image processing complex algorithms here. 

Created on Nov 19, 2011

@author: Julien Lengrand-Lambert
'''

import cv

def create_same_image(in_img, zero=0):
    """
    Creates an image of same size, depth and number of channels as input image
    If zero is activated, the image content is set to 0.
    
    If creation fails, function returns an Error.  
    """
    try :
        out_img = cv.CreateImage(cv.GetSize(in_img), 
                                 in_img.depth, 
                                 in_img.nChannels)
    except TypeError:
        print "ERROR : (create_same_image): Image creation failed!"
    
    if zero:
        try:
            cv.Zero(out_img)
        except TypeError:
            print "ERROR : (create_same_image): Image erasing failed!"
        
    return out_img