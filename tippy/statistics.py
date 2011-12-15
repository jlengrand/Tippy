'''
Contains functions related to statistics processing. 

Created on Dec 11, 2011

@author: Julien Lengrand-Lambert
@email: julien@lengrand.fr
'''

import cv
import sys

class Histogram():
    """
    This class is designed to contain an openCV class plus some more information
    to ease further operations.
    
    NOTE : Supports only 1 channel / 8 bits images for now. 
    More should be added soon.    
    """
    def __init__(self):
        self.cvhist = None
        self.min_range = 0
        self.depth = cv.IPL_DEPTH_8U
        self.nb_bins = 0 
        self.channels = 0
    
    def compute_histogram(self, img, bin_fact=cv.IPL_DEPTH_8U, min_range=0):
        """
        Creates the histogram of the input image
        
        Returns a Tippy histogram, with one item by channel of input image.
        The number of bins is 2^bin_fact (256 by default)
        min_range is the value of the lowest bin
        max_range is automatically calculated using the input image depth. 
        max_range = (2^img_depth)
        
        NOTE : Supports only 1 channel / 8 bits images for now. 
        More should be added soon.
        """
        # TESTS
        try:
            cv.GetSize(img)
        except TypeError:
            raise TypeError("(%s) img : IplImage expected!" 
                            % (sys._getframe().f_code.co_name))
        
        # img test
        if not(img.depth == cv.IPL_DEPTH_8U):
            raise TypeError("(%s) 8U image expected!" 
                            % (sys._getframe().f_code.co_name))
        elif not(img.nChannels is 1):
            raise TypeError("(%s) 1C image expected!" 
                            % (sys._getframe().f_code.co_name))
        
        # bin_fact test
        if (bin_fact <= 0 or ((bin_fact % 2) != 0)):
            raise ValueError("(%s) Positive odd integer expected!" 
                             % (sys._getframe().f_code.co_name))
        elif type(bin_fact) not in [int, long]:
            raise TypeError("(%s) Positive odd integer expected!" 
                            % (sys._getframe().f_code.co_name))

        # min_range test
        if type(min_range) != int:
            raise TypeError("(%s) Positive odd integer expected!" 
                            % (sys._getframe().f_code.co_name))  
            
        self.channels = img.nChannels
        self.nb_bins = int(pow(2, bin_fact))
        self.depth = int(img.depth)
        max_range = pow(2, self.depth)
        self.ranges = [min_range, max_range]
    
        dims = [self.nb_bins]
        all_ranges = [self.ranges]
        
        self.cvhist = cv.CreateHist( dims, 
                                     cv.CV_HIST_ARRAY, 
                                     all_ranges, 
                                     uniform=1)
        cv.CalcHist([img], self.cvhist)    
        
    def hist2table(self):
        """
        Transform an histogram into a list of values.
        This way, it is easier to process for calculations.
        
        NOTE : Supports only 1 channel / 8 bits images for now. 
        More should be added soon.    
        """        
        if self.nb_bins < 1:
            raise TypeError("(%s) Histogram expected!" 
                            % (sys._getframe().f_code.co_name))
        
        histable = []
        for jj in range(self.nb_bins):                
            histable.append(self.cvhist.bins[jj])
    
        return histable
    
    def hist2image(self, scale_x=3, scale_y=3, y_range=64):
        """
        Creates an iplimage displaying histogram results after its computation
        # TODO : might be used with histable too ? 
        """
        if self.nb_bins < 1:
            raise TypeError("(%s) Histogram expected!" 
                            % (sys._getframe().f_code.co_name))

        if ((type(scale_x) != int) or (scale_x <= 0)):
            raise TypeError("(%s) Positive integer expected!" 
                            % (sys._getframe().f_code.co_name)) 
    
        if ((type(scale_y) != int) or (scale_y <= 0)):
            raise TypeError("(%s) Positive integer expected!" 
                            % (sys._getframe().f_code.co_name))      
            
        if ((type(y_range) != int) or (y_range <= 0)):
            raise TypeError("(%s) Positive integer expected!" 
                            % (sys._getframe().f_code.co_name))
            
        max_range = self.ranges[1] - 1
        (_, hist_max, _, _ ) = cv.GetMinMaxHistValue(self.cvhist)
        hist_img = cv.CreateImage( (max_range*scale_x, y_range*scale_y),
                                    self.depth,
                                    self.channels)        
        cv.Zero(hist_img) # resets image values
                            
        for i in range(max_range): # 0 to max_range
            hist_value = cv.QueryHistValue_1D(self.cvhist, i)
            next_value = cv.QueryHistValue_1D(self.cvhist, i+1)
            pt1 = ( int(i*scale_x),
                    int(y_range*scale_y))
            pt2 = ( int(i*scale_x+ scale_x), 
                int(y_range*scale_y))
            pt3 = ( int(i*scale_x+scale_x), 
                int((y_range-(next_value*y_range/hist_max))*scale_y))
            pt4 = ( int(i*scale_x), 
                int((y_range-(hist_value*y_range/hist_max))*scale_y))
            pts = (pt1, pt2, pt3, pt4)
            cv.FillConvexPoly(hist_img, pts, 255, lineType=8, shift=0)

        return hist_img