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
        self.img_1c = cv.LoadImage("data/tippy.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE) # 1 channel image 
        self.img_3c = cv.LoadImage("data/tippy.jpg", cv.CV_LOAD_IMAGE_COLOR) # 3 channel image 
        self.img_16s = cv.CreateImage((15, 15), cv.IPL_DEPTH_16S, 1) # Non 8 bits image
        self.fake_img = 10 # non Image

        self.dims = cv.GetSize(self.img_1c)
        
        self.thres = 1
        self.neg_thres = -10
        self.bad_thres = "A"
        
        self.seed = (10, 10)
        self.neg_seed = (-10, 10)
        self.big_seed = (10, self.dims[1] + 5)
        self.bad_seed = 10
        self.long_seed = (10, 10, 10)

        self.conn = 4
        self.bad_conn = "A"
        self.h_conn = 8
        self.other_conn = 16

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
        self.assertRaises(TypeError, lambda: se.simple_region_growing(self.fake_img, self.seed))
        
        # Threshold tests
        self.assertRaises(ValueError, lambda: se.simple_region_growing(self.img_1c, self.seed, self.neg_thres))
        self.assertRaises(TypeError, lambda: se.simple_region_growing(self.img_1c, self.seed, self.bad_thres))
        # Seed tests
        self.assertRaises(ValueError, lambda: se.simple_region_growing(self.img_1c, self.neg_seed))
        self.assertRaises(ValueError, lambda: se.simple_region_growing(self.img_1c, self.big_seed))
        self.assertRaises(TypeError, lambda: se.simple_region_growing(self.img_1c, self.bad_seed))
        self.assertRaises(TypeError, lambda: se.simple_region_growing(self.img_1c, self.long_seed))
        # output test
        out_img = se.simple_region_growing(self.img_1c, self.seed)
        self.assertEqual(out_img.depth, cv.IPL_DEPTH_8U)
        self.assertEqual(out_img.nChannels, 1)
        self.assertEqual(cv.GetSize(out_img), cv.GetSize(self.img_1c))
        # connectivity test
        self.assertRaises(TypeError, lambda: se.simple_region_growing(self.img_1c, self.seed, self.thres, self.bad_conn))
        self.assertRaises(ValueError, lambda: se.simple_region_growing(self.img_1c, self.seed, self.thres, self.other_conn))
        # function result tests
        # 4-conn
        img_gnu = cv.LoadImage("data/gnu.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE) # 1 channel image 
        out_img = se.simple_region_growing(img_gnu, seed=(70, 106), threshold=20)
        self.assertEqual(cv.CountNonZero(out_img), 584)
        # 8-conn
        img_gnu = cv.LoadImage("data/gnu.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE) # 1 channel image 
        out_img = se.simple_region_growing(img_gnu, seed=(70, 106), threshold=20, conn=8)
        self.assertEqual(cv.CountNonZero(out_img), 627)
                   
#if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()