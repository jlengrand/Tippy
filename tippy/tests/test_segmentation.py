'''"
Created on Nov 26, 2011

@author: Julien Lengrand-Lambert
@email: julien@lengrand.fr
'''
import unittest
import cv

import tippy.segmentations as se

class Test(unittest.TestCase):


    def setUp(self):
        """
        This method is called before each test
        """
        self.img_1c = cv.LoadImage("../data/tippy.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE) # 1 channel image 
        self.img_3c = cv.LoadImage("../data/tippy.jpg", cv.CV_LOAD_IMAGE_COLOR) # 3 channel image 
        self.img_16s = cv.CreateImage((15, 15), cv.IPL_DEPTH_16S, 1) # Non 8 bits image
        self.fake_img = 10 # non Image
    
        self.dims = cv.GetSize(self.img_1c)
        
        self.neg_thres = -0
        self.bad_thres = "A"
        
        self.seed = (10, 10)
        self.neg_seed = (-10, 10)
        self.big_seed = (10, self.dims[1] + 5)
        self.bad_seed = 10
        self.long_seed = (10, 10, 10)

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    #--- 
    ## TESTS
    def test_region_growing(self):
        # Image type tests
        self.assertRaises(TypeError, lambda: se.simple_region_growing(self.img_3c, self.seed))
        self.assertRaises(TypeError, lambda: se.simple_region_growing(self.img_16s, self.seed))
        # Threshold tests
        self.assertRaises(ValueError, lambda: se.simple_region_growing(self.img_1c, self.seed, self.neg_thres))
        self.assertRaises(TypeError, lambda: se.simple_region_growing(self.img_1c, self.seed, self.bad_thres))
        # Seed tests
        self.assertRaises(ValueError, lambda: se.simple_region_growing(self.img_1c, self.neg_seed))
        self.assertRaises(ValueError, lambda: se.simple_region_growing(self.img_1c, self.big_seed))
        self.assertRaises(TypeError, lambda: se.simple_region_growing(self.img_1c, self.bad_seed))
        self.assertRaises(TypeError, lambda: se.simple_region_growing(self.img_1c, self.long_seed))
        # output test
        out_img = simple_region_growing(self.img_1c, self.seed)
        self.assertEqual(out_img.depth, cv.IPL_DEPTH_8U)
        self.assertEqual(out_img.nChannels, 1)
        self.assertEqual(cv.GetSize(out_img), cv.GetSize(self.img_1C))
           
#if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()