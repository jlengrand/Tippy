'''
Created on Dec 11, 2011

@author: Julien Lengrand-Lambert
@email: julien@lengrand.fr
'''
import unittest
import cv

import tippy.statistics as st

class Test(unittest.TestCase):


    def setUp(self):
        """
        This method is called before each test
        """
        self.img_1c = cv.LoadImage("data/tippy.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE) # 1 channel image 
        self.img_3c = cv.LoadImage("data/tippy.jpg", cv.CV_LOAD_IMAGE_COLOR) # 3 channel image 
        self.img_16s = cv.CreateImage((15, 15), cv.IPL_DEPTH_16S, 1) # Non 8 bits image
        
        self.val = 10 # non Image
        self.neg_val = -10 # non Image
        self.string = "A" # non Image

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    #--- 
    ## TESTS
    def test_compute_histogram(self):
        # testing input image
        # st.compute_histogram(self.img_1c)
        self.assertRaises(TypeError, lambda: st.compute_histogram(self.val) )
        self.assertRaises(TypeError, lambda: st.compute_histogram(self.img_3c) )        
        
        # testing bin_fact
        self.assertRaises(ValueError, lambda: st.compute_histogram(self.img_1c, self.neg_val) )
        self.assertRaises(TypeError, lambda: st.compute_histogram(self.img_1c, self.string) ) 

        # testing min_range. It can be either negative or even.
        self.assertRaises(TypeError, lambda: st.compute_histogram(self.img_1c, self.val, self.string) ) 

    def test_hist2table(self):
        # testing input histogram
        # hist = st.compute_histogram(self.img_1c)
        self.assertRaises(TypeError, lambda: st.hist2table(self.val))
        
#if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()