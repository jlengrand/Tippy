'''
Contains functions related to statistics processing. 

Created on Dec 11, 2011

@author: Julien Lengrand-Lambert
@email: julien@lengrand.fr
'''

import cv
import sys

def compute_histogram(img, bin_fact=cv.IPL_DEPTH_8U, min_range=0):
    """
    This function is designed to create the color histogram of the image in 
    input.
    Returns a list of histograms, with one item by channel of input image.
    The number of bins is 2^bin_fact (256 by default)
    min_range is the lowest bin taken. max_range is automatically calculated with 
    the input image depth. (2^img_depth)
    
    NOTE : Supports only 1 channel / 8 bits images for now. 
    More should be added soon.
    """
    try:
        cv.GetSize(img)
    except TypeError:
        raise TypeError("(%s) img : IplImage expected!" % (sys._getframe().f_code.co_name))
    
    # img test
    if not(img.depth == cv.IPL_DEPTH_8U):
        raise TypeError("(%s) 8U image expected!" % (sys._getframe().f_code.co_name))
    elif not(img.nChannels is 1):
        raise TypeError("(%s) 1C image expected!" % (sys._getframe().f_code.co_name))
    
    # bin_fact test
    if (bin_fact <= 0 or ((bin_fact % 2) != 0)):
        raise ValueError("(%s) Positive odd integer expected!" % (sys._getframe().f_code.co_name))
    elif type(bin_fact) not in [int, long]:
        raise TypeError("(%s) Positive odd integer expected!" % (sys._getframe().f_code.co_name))

    # min_range test
    if type(min_range) != int:
        raise TypeError("(%s) Positive odd integer expected!" % (sys._getframe().f_code.co_name))    
    
    bins = pow(2, bin_fact)
    max_range = pow(2, img.depth)
    ranges = [min_range, max_range]

    dims = [bins]
    all_ranges = [ranges]
    
    hist = cv.CreateHist( dims, cv.CV_HIST_ARRAY, all_ranges, uniform=1)
    cv.CalcHist([img], hist)

    return hist

def hist2table(hist):
    """
    Transform an histogram into a (numpy) table of values.
    This way, it is easier to process for calculations.
    
    NOTE : Supports only 1 channel / 8 bits images for now. 
    More should be added soon.    
    """
    try:
        hist.bins
    except AttributeError:
        raise TypeError("(%s) Histogram expected!" % (sys._getframe().f_code.co_name))   
    # TO BE CONTINUED . . . 
    pass
    