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
        self.img_2c = cv.CreateImage((10, 10), cv.IPL_DEPTH_8U, 2) # fake 2 channels image 
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
        self.assertRaises(TypeError, lambda:st.Histogram(self.val) )
        self.assertRaises(TypeError, lambda:st.Histogram(self.img_16s) )        
        self.assertRaises(ValueError, lambda:st.Histogram(self.img_2c) )      
        # testing bin_fact
        self.assertRaises(ValueError, 
                          lambda: st.Histogram(self.img_1c, self.neg_val))
        self.assertRaises(TypeError, 
                          lambda: st.Histogram(self.img_1c, self.string)) 

        # testing min_range. It can be either negative or even.
        self.assertRaises(TypeError, 
                          lambda: st.Histogram(self.img_1c, self.val, self.string))     

        # testing output
        hist_1c = st.Histogram(self.img_1c)
        self.assertEquals(self.img_1c.nChannels, hist_1c.channels)     
        hist_3c = st.Histogram(self.img_3c)
        self.assertEquals(self.img_3c.nChannels, hist_3c.channels)

    def test_hist2table(self):
        # testing output size 
        hist = st.Histogram(self.img_3c)
        histable = hist.hist2table()
        self.assertEqual(3, len(histable))
        self.assertEqual(256, len(histable[0]))
        
    def test_hist2image(self):     
        hist = st.Histogram(self.img_1c)
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