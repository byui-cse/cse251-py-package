from setuptools import setup

setup(
    name='cse251',
    version='0.0.1',
    description='The package that contains common classes for the BYU Idaho CSE 251 course',
    url='https://github.com/byui-cse/cse251-course-files',
    author='Luc Comeau and Hunter Wilhelm',
    license='none',
    packages=['cse251'],
    install_requires=['matplotlib', 'numpy', 'pillow', 'opencv-python', 'requests'],
    zip_safe=False
)