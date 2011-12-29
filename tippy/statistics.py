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
    
    NOTE : Supports only 8 bits images for now. 
    More should be added soon.    
    """
    def __init__(self, img, bin_fact=cv.IPL_DEPTH_8U, min_range=0):
        self.cvhist = None
        self.min_range = 0
        self.depth = cv.IPL_DEPTH_8U
        self.nb_bins = 0 
        self.channels = 0
        self.compute_histogram(img, bin_fact, min_range)
    
    def compute_histogram(self, img, bin_fact=cv.IPL_DEPTH_8U, min_range=0):
        """
        Creates the histogram of the input image
        
        Returns a Tippy histogram, with one item by channel of input image.
        The number of bins is 2^bin_fact (256 by default)
        min_range is the value of the lowest bin
        max_range is automatically calculated using the input image depth. 
        max_range = (2^img_depth)
        
        NOTE : Supports only 8 bits images for now. 
        More should be added soon.
        """
        # TESTS
        try:
            dims = cv.GetSize(img)
        except TypeError:
            raise TypeError("(%s) img : IplImage expected!" 
                            % (sys._getframe().f_code.co_name))
        
        # img test
        #if not(img.depth == cv.IPL_DEPTH_8U):
        #    raise TypeError("(%s) 8U image expected!" 
        #                    % (sys._getframe().f_code.co_name))
        if img.nChannels not in [1, 3]:
            raise ValueError("(%s) 1 or 3 channels image expected!" 
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
        max_range = pow(2, bin_fact) + min_range - 1
        self.ranges = [min_range, max_range]
        
        img_list = []
        # preparing images depending on nChannels
        if self.channels == 1:
            img_list = [img]
        elif self.channels == 3:
            # TODO: change this into function
            img_1 = cv.CreateImage(dims, cv.IPL_DEPTH_8U, 1)
            img_2 = cv.CreateImage(dims, cv.IPL_DEPTH_8U, 1)
            img_3 = cv.CreateImage(dims, cv.IPL_DEPTH_8U, 1)
            
            cv.Split(img, img_1, img_2, img_3, None)            
            img_list = [img_1, img_2, img_3]
            
        self.cvhist = self._compute_1ch_histogram(img_list)
        
    def _compute_1ch_histogram(self, img_list):
        """
        DESIGNED FOR INTERNAL USE ONLY
        CAREFUL, NO VERIFICATIONS PERFORMED
        """
        dims = [self.nb_bins]
        all_ranges = [self.ranges]
        
        hist_list = [] 
        for img in img_list:
            hist = cv.CreateHist( dims, 
                                  cv.CV_HIST_ARRAY, 
                                  all_ranges, 
                                  uniform=1)
            cv.CalcHist([img], hist)
            hist_list.append(hist)   

        return hist_list
        
    def to_tables(self):
        """
        Transforms an histogram into a list of values.
        This way, it is easier to process for calculations.
        
        Returns a list of nChannels items.
        
        NOTE : Supports only 8 bits images for now. 
        More should be added soon.        
        """        
        if self.nb_bins < 1:
            raise TypeError("(%s) Histogram expected!" 
                            % (sys._getframe().f_code.co_name))
        
        histable = []
        for ii in range(self.channels):
            hist_list = []
            for jj in range(self.nb_bins):                
                hist_list.append(self.cvhist[ii].bins[jj])
            histable.append(hist_list)
        return histable

    def to_images(self, scale_x=3, scale_y=3, y_range=64):
        """
        Creates a graphical representation of an histogram.
        Outputs a list of nChannels iplimages, one for each channel of the 
        histogram. 
        The images should have the same depth as the image used to create the 
        histogram.  
        """
        if ((type(scale_x) != int) or (scale_x <= 0)):
            raise TypeError("(%s) Positive integer expected!" 
                            % (sys._getframe().f_code.co_name)) 
    
        if ((type(scale_y) != int) or (scale_y <= 0)):
            raise TypeError("(%s) Positive integer expected!" 
                            % (sys._getframe().f_code.co_name))      
            
        if ((type(y_range) != int) or (y_range <= 0)):
            raise TypeError("(%s) Positive integer expected!" 
                            % (sys._getframe().f_code.co_name))

        images = []
        for jj in range(self.channels):
            images.append(self.channel_to_image(jj + 1, 
                                                scale_x, 
                                                scale_y, 
                                                y_range))
            
        return images
                            
    def channel_to_image(self, chan, scale_x=3, scale_y=3, y_range=64):
        """
        Creates an iplimage displaying histogram results after its computation
        """
        if ((type(chan) != int) or (chan <= 0)):
            raise TypeError("(%s) Positive integer expected!" 
                            % (sys._getframe().f_code.co_name))         
        elif chan > self.channels:
            raise ValueError("(%s) Incoherent channel selected!" 
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
        (_, hist_max, _, _ ) = cv.GetMinMaxHistValue(self.cvhist[chan - 1])
        hist_img = cv.CreateImage( (max_range*scale_x, y_range*scale_y),
                                    self.depth,
                                    1)        
        cv.Zero(hist_img) # resets image values
                            
        for i in range(max_range): # 0 to max_range
            hist_value = cv.QueryHistValue_1D(self.cvhist[chan - 1], i)
            next_value = cv.QueryHistValue_1D(self.cvhist[chan - 1], i+1)
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
    
    
