# [TIPPY](http://dl.dropbox.com/u/4286043/00_Website/03_Images/TIPPY.jpg) : another Toolbox for Image Processing in PYthon

This repository contains all sources and installer of the Tippy project. 
Tippy is a set of functions and methods designed to reduce as much as possible the code needed to deploy an Image Processing/Computer Vision algorithm. 
It is based on the famous [OpenCV](http://opencv.willowgarage.com/wiki/) library and its [Python bindings](http://opencv.willowgarage.com/wiki/PythonInterface).

OpenCV is one of the most famous Computer Vision library in the world, and surely the most famous one in the open-source one. It provides more than 500 functions, from basic one to complete and complex methods. It is mainly implemented in C code, but now supports lots of languages and platforms (C++, java, iphone and android, ...). 

This project aims at magnifying the power of OpenCV in using the power of Python. The idea is to get as much results as possible with as little code as possible. In this way, this code will keep using well known OpenCV structures (such as cvMat or IplImage) while simplifying its use. 


Here is a simple example. Let's imagine we have an RGB image, and we want to display it in HSV space. 
The Python OpenCV code would be:

`
import cv 
img = cv.LoadImage('test.jpg')
imgHSV = cv.CreateImage( cv.GetSize(img), img.depth, img.nChannels)
cv.CvtColor(img, imgHSV, cv.CV_RGB2HSV)
cv.NamedWindow("HSV display")
cv.ShowImage("HSV display", imgHSV)
cv.WaitKey(0)
`

The same code using Tippy would give :

`
import cv
import tippy as tp
img = cv.LoadImage('test.jpg')
imgHSV = tp.RGB2HSV(img)
tp.DisplayWait("HSV display", imgHSV, 0)
`

Hence, the main objective is to keep the best of OpenCV while reducing the amount of code needed to get things working smoothly. Tippy contains templates in which you simply have to fill the parts corresponding to your precise needs.


Tippy mostly aims at :
- being an efficient Prototyping tool by reducing the time needed to deploy a Computer Vision algorithm and see its results
- being cross-platform and robust. All functions have a corresponding test. 
- enhancing lacks in the OpenCV library, such as region growing algorithms. . .
- allowing a fast mastering of the library with the production of complete examples. 
- allowing anyone to enhance the library capabilities, by using simple and clear code conventions.


Please note that the library is in current development, and is only available as source code for now. This explains why the bin folder is still empty. 


## Installation

To use Tippy, you will need the last OpenCV version with Python bindings. A descriptive tutorial for Linux systems can be found [here](http://opencv.willowgarage.com/wiki/InstallGuide%20%3A%20Debian).

Being in the very beginning of its development, Tippy yet is not available in packaged version. To use it, you will need to downlad the source file and include them in your application. 

The action is pretty straightforward though:
- Download the tippy folder of the Tippy project
- Place it in your working directory.
- import parts of the library as you wish by using 'import file' in your python code. 

## Hints and Usage

Important points of Tippy are documentation and examples. 
An example will be create for every single function present in the Tippy package, so that it can easily be used by everyone. 
In addition, tests should be carried out so that the code contain as few hidden bugs as possible.

Finally, functions should be heavily documented to help users dig in without encounter language problems. 

I am currently thinking about generating a more complete and redable documentation, such as html output. It should come soon.

## Copyright

Copyright © 2011 Julien Lengrand-Lambert

Files are licensed under the under the BSD License. See the file COPYING for details.
You are free to use it as you wish, but I would love if you let me know ^^

Image: Paul Martin Eldridge / FreeDigitalPhotos.net

## Contact

I would enjoy having feedback if you use this theme. 
Feel free to mail me for any comment or request. 

You can contact me at jlengrand at gmail dot com, or in my [current website](http://www.lengrandlambert.fr)
