'''
Tippy : another Toolbox for Image Processing in PYthon

Created on Nov 19, 2011
Copyright (C) 2011  Julien Lengrand-Lambert <julien@lengrand.fr>

@author: Julien Lengrand-Lambert
@email: julien@lengrand.fr
'''
try:
    import cv
except:
    print ''
    print 'Tippy requires the latest OpenCV Python bindings'
    print 'See: http://opencv.willowgarage.com/wiki// for OpenCV installation'
    print 'and http://opencv.willowgarage.com/wiki/PythonInterface for Python bindings'
    sys.exit(0)

from distutils.core import setup

setup(
    name='Tippy',
    version='0.1',
    author='Julien Lengrand-Lambert',
    author_email='julien@lengrand.fr',
    packages=['tippy', 'tippy.tests', 'tippy.examples'],
    package_data={'tippy': ['data/*.*']},
    url='https://github.com/jlengrand/Tippy',
    license='LICENSE.txt',
    description='another Toolbox for Image Processing in PYthon, based on OpenCV',
    long_description=open('README.txt').read(),
    classifiers = ['Development Status :: 2 - Pre-Alpha',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Environment :: Console',
                   'Environment :: Plugins',
                   'Operating System :: OS Independent',
                   'Operating System :: Unix',
                   'Programming Language :: Python ',
                   'Programming Language :: C ',
                   'Natural Language :: English ',
                   'Topic :: Utilities',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Software Development'],
)