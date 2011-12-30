======================================================
Tippy : another Toolbox for Image Processing in PYthon
======================================================


Tippy is a set of functions and methods designed to reduce as much as possible the code needed to deploy an <Image Processing> or <Computer Vision> algorithm. It is based on the famous <OpenCV> library and its Python bindings.

OpenCV is one of the most famous Computer Vision library in the world, and surely the most famous one in the open-source one. It provides more than 500 functions, from basic one to complete and complex methods. 
It is mainly implemented in C code, but now supports lots of languages and platforms (C++, java, iphone and android, ...). 

This project aims at magnifying the power of OpenCV in using the power of Python. The idea is to get as much results as possible with as little code as possible. 
In this way, this code will keep using well known OpenCV structures (such as cvMat or IplImage) while simplifying its use. 


Let's imagine we have an RGB image, and we want to display the histogram of its blue channel values.
Typical usage often looks like this::

    #!/usr/bin/env python
	import cv
	from tippy import statistics as st
	from tippy import display_operations as do
	
	# test with 8 bits color image
	img_name = "tippy/data/tippy.jpg"
	img = cv.LoadImage(img_name, cv.CV_LOAD_IMAGE_COLOR)
	hist = st.Histogram(img)
	    
	imgs = hist.to_images() # list of Red, Green, Blue channels
	do.display_single_image(imgs[2], "Blue channel histogram of the tippy image")


**Please note that the library is in current development, and is only available as source code for now. This explains why the bin folder is still empty.**


A Installation
==============

To use Tippy, you will need the last OpenCV version with Python bindings. A descriptive tutorial for Linux systems can be found `here <http://opencv.willowgarage.com/wiki/InstallGuide%20%3A%20Debian>`_.

To be sure that you can use tippy, simply run python in command line and try to import OpenCV ::

	Python 2.7.2+ (default, Oct  4 2011, 20:03:08) 
	[GCC 4.6.1] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import cv

If no error appears, Tippy shouold be installed without problems. 	


Being in the very beginning of its development, Tippy yet is not available in packaged version. To use it, you will need to download the source file and include them in your application. 

The action is pretty straightforward though:
* Download the tippy folder of the Tippy project
* Place it in your working directory.
* import parts of the library as you wish by using 'import file' in your Python code. 

B Hints and Usage
=================

Important points of Tippy are documentation and examples. 
An example will be create for every single function present in the Tippy package, so that it can easily be used by everyone. 
In addition, tests should be carried out so that the code contain as few hidden bugs as possible.

Finally, functions should be heavily documented to help users dig in without encounter language problems. 

I am currently thinking about generating a more complete and readable documentation, such as html output. It should come soon.

C Copyright
===========

Copyright © 2011 Julien Lengrand-Lambert

Files are licensed under the under the BSD License. See the file LICENCE.txt for details.
You are free to use it as you wish, but I would love if you let me know ^^

Image: Paul Martin Eldridge / FreeDigitalPhotos.net
 
 
D Contact
=========

I would enjoy having feedback if you use this theme. 
Feel free to mail me for any comment or request. 

You can contact me at julien@lengrand.fr, or on `my current website <http://www.lengrand.fr>`_.