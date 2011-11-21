'''
Contains all tests for basic_operations module
Tests are actually run at execution in the end of module. 

Created on Nov 19, 2011

@author: Julien Lengrand-Lambert
'''

import unittest
import cv
import tippy.basic_operations as bo

class Test(unittest.TestCase):
    """
    The class herits from unittest
    """
    def setUp(self):
        """
        This method is called before each test
        """
        self.img_1c = cv.LoadImage("../data/tippy.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE) # 1 channel image 
        self.img_3c = cv.LoadImage("../data/tippy.jpg", cv.CV_LOAD_IMAGE_COLOR) # 1 channel image 
    def tearDown(self):
        """
        This method is called after each test
        """ 
        pass
    #-------- 
    ## TESTS
    def test_create_same_image(self):
        out_img = bo.create_same_image(self.img_1c)
        self.assertEqual(self.img_1c.nChannels, out_img.nChannels)
        self.assertEqual(self.img_1c.depth, out_img.depth)
        self.assertEqual(cv.GetSize(self.img_1c), cv.GetSize(out_img))
                
if __name__ == '__main__':
    unittest.main()