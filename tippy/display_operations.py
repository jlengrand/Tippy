'''
Contains all functions related to graphical display.

Created on Nov 19, 2011

@author: Julien Lengrand-Lambert

'''

import sys
import cv

def display_single_image(img, name="Image", x_pos=0, y_pos=0, wait=0):
    """
    Displays an image on screen.
    Position can be chosen, and time on screen too.
    Wait is diplay time, in milliseconds.
    If wait =0, the Image stays on screen until user interaction.
    ----
    Ex:
    img = cv.LoadImage("../data/tippy.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE)
    display_single_image(img, "My Tippy", 0, 0, 100)
    """
    #TODO: Still not implemented!
    pass