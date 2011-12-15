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
        hist = st.Histogram()
        # testing input image
        self.assertRaises(TypeError, lambda:hist.compute_histogram(self.val) )
        self.assertRaises(TypeError, lambda:hist.compute_histogram(self.img_3c))       
    
        # testing bin_fact
        self.assertRaises(ValueError, 
                          lambda: hist.compute_histogram(self.img_1c, self.neg_val))
        self.assertRaises(TypeError, 
                          lambda: hist.compute_histogram(self.img_1c, self.string)) 

        # testing min_range. It can be either negative or even.
        self.assertRaises(TypeError, 
                          lambda: hist.compute_histogram(self.img_1c, self.val, self.string))     

    def test_hist2table(self):
        hist = st.Histogram()
        # testing input histogram        
        self.assertRaises(TypeError, lambda: hist.hist2table(self.val))
        # testing output size 
        hist.compute_histogram(self.img_1c)
        histable = hist.hist2table()
        self.assertEqual(256, len(histable))
        
    def test_hist2image(self):
        hist = st.Histogram()
        # testing input histogram
        self.assertRaises(TypeError, lambda: hist.hist2image(self.val))        
        # testing scale inputs 
        self.assertRaises(TypeError, 
                          lambda: hist.hist2image(hist, self.string))
        self.assertRaises(TypeError, 
                          lambda: hist.hist2image(hist, self.neg_val))
        self.assertRaises(TypeError, 
                          lambda: hist.hist2image(hist, self.val, self.string))
        self.assertRaises(TypeError, 
                          lambda: hist.hist2image(hist, self.val, self.neg_val))
        # testing range inputs
        self.assertRaises(TypeError, 
                          lambda: hist.hist2image(hist, self.val, self.val, self.string))
        self.assertRaises(TypeError, 
                          lambda: hist.hist2image(hist, self.val, self.val, self.neg_val))     
#if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()