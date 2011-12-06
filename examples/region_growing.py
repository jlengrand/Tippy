'''
Created on Nov 28, 2011

@author: Julien Lengrand-Lambert
@email: julien@lengrand.fr
---
Here is a simple example of (simple) Region Growing algorithm in Python. 

A word about region growing (taken from Wikipedia), and this implementation : 
"Region growing is a simple region-based image segmentation method. It is also classified as a pixel-based image segmentation method since it involves the selection of initial seed points.
This approach to segmentation examines neighboring pixels of initial "seed points" and determines whether the pixel neighbors should be added to the region. The process is iterated on, in the same manner as general data clustering algorithms"
Basically, region growing is an iterative method used to extract similar parts of an image. One or several points are chosen as a start. The region then grows until it is finally blocked by the stop criteria. This criteria is generally an inside/outside region comparison (energy, size, . . .).
Region growing is massively used in medical imaging, and object detection. Here is an example of application in automatic Mine Hunting, which I worked with last year at TNO. 

The following method uses one seed point, defined by the user. The region grows by comparing with its neighbourhood. The chosen criteria is in this case a difference between outside pixel's intensity value and the region's mean.
The pixel with minimum intensity in the region neighbouhood is chosen to be included. The growing stops as soon as the difference is larger than a threshold. 

In this implementation, a 4-connectivity has been chosen. The 8-connectivity should be included soon. 
Due to the method itself, only grayscale images may be processed for now. So color images should be converted first. 

'''

import cv
import tippy.segmentations as se
import tippy.basic_operations as bo
import tippy.display_operations as do


user_input = 0

img_name = "tippy/data/gnu.jpg"
threshold = 20
connectivity = 8
img = cv.LoadImage(img_name, cv.CV_LOAD_IMAGE_GRAYSCALE)

if user_input:
    seed = bo.mouse_point(img, mode="S") # waits for user click to get seed
else:
    seed = (70, 106)

out_img = se.simple_region_growing(img, seed, threshold, connectivity)

do.display_single_image(out_img, "Region Growing result")
