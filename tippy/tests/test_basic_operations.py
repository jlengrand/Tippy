'''
Contains all tests for basic_operations module

Created on Nov 19, 2011

@author: Julien Lengrand-Lambert
@email: julien@lengrand.fr
'''

import cv
import unittest

import tippy.basic_operations as bo

class Test(unittest.TestCase):
    """
    The class inherits from unittest
    """
    def setUp(self):
        """
        This method is called before each test
        """
        self.img_1c = cv.LoadImage("data/tippy.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE) # 1 channel image 
        self.img_3c = cv.LoadImage("data/tippy.jpg", cv.CV_LOAD_IMAGE_COLOR) # 3 channel image 
        self.img_fake_2c = cv.CreateImage((15, 15), cv.IPL_DEPTH_8U, 2) # 2 channels
        self.fake_img = 10 # non Image
        
        self.false_mode = "A" # non True/False (or 0/1) argument
        self.fake_mode = 100 # non True/False (or 0/1) argument
        self.fake_name = 100 # non True/False (or 0/1) argument
        
    def tearDown(self):
        """
        This method is called after each test
        """ 
        pass
    #--- 
    ## TESTS
    def test_create_same_image(self):
        for img in (self.img_1c, self.img_3c):
            #tests 1 and 3 channels images
            out_img = bo.create_same_image(img, 1)
            self.assertEqual(img.nChannels, out_img.nChannels)
            self.assertEqual(img.depth, out_img.depth)
            self.assertEqual(cv.GetSize(img), cv.GetSize(out_img))
        self.assertRaises(TypeError, lambda: bo.create_same_image(self.fake_img))

    def test_mouse_point(self):
        # img test
        self.assertRaises(TypeError, lambda: bo.mouse_point(self.fake_img))
        # name test
        self.assertRaises(TypeError, lambda: bo.mouse_point(self.img_3c, self.fake_name))
        # mode test
        self.assertRaises(TypeError, lambda: bo.mouse_point(self.img_3c, mode=self.fake_mode))
        self.assertRaises(ValueError, lambda: bo.mouse_point(self.img_3c, mode=self.false_mode))
        # TODO: How to test arguments that need user interaction?
        
#if __name__ == "__main__":
    #unittest.main()