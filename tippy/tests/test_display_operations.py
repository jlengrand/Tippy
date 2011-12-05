'''
Contains all tests for display_operations module

Created on Nov 24, 2011

@author: Julien Lengrand-Lambert
@email: julien@lengrand.fr
'''
import unittest
import cv

import tippy.display_operations as do

class Test(unittest.TestCase):
    """
    This class inherits from unittest
    """
    def setUp(self):
        """
        This method is called before each test
        """
        self.img = cv.LoadImage("data/tippy.jpg", cv.CV_LOAD_IMAGE_COLOR) # 3 channel image 
        self.fake_img = 10 # non Image        

    def tearDown(self):
        """
        This method is called after each test
        """         
        pass

    #---
    ## TESTS
    def test_display_single_image(self):
        #exception still to be found!
        self.assertRaises(TypeError, lambda: do.display_single_image(self.img, x_pos="A"))
        self.assertRaises(TypeError, lambda: do.display_single_image(self.img, name=2))
        self.assertRaises(TypeError, lambda: do.display_single_image(self.fake_img ))

#if __name__ == "__main__":
    #unittest.main()