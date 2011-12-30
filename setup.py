from distutils.core import setup

setup(
    name='Tippy',
    version='0.1',
    author='Julien Lengrand-Lambert',
    author_email='julien@lengrand.fr',
    packages=['tippy', 'tippy.tests', 'examples'],
    url='https://github.com/jlengrand/Tippy',
    license='LICENSE.txt',
    description='another Toolbox for Image Processing in PYthon, based on OpenCV',
    long_description=open('README.txt').read(),
    install_requires=[
        "OpenCV >= 3.1",
    ],
)