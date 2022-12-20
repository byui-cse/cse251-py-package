# CSE251 Library

The package that contains common classes for the CSE 251 course.

## Instructions

Run in the console
```bash
Mac:
python3 -m pip install git+https://github.com/byui-cse/cse251-course-files.git

Windows:
<full path of python> -m pip install git+https://github.com/byui-cse/cse251-course-files.git
```
(Use `python` or `python3` depending on your environment)

And to use it

```python
from cse251 import *
```

## Authors
* Luc Comeau
* [Hunter Wilhelm](https://github.com/hunterwilhelm)

## Overview
It provides:
* setting the current working directory
* convenient logging to stdout and file
* load json files
* provides plot support from matplotlib

Using pip has the following advantages:
* more flexible running experience (working directory)
* includes Intellisense instead of showing unknown function
* able to be updated without modifying other repositories

It pip installs the following:
* matplotlib
* numpy
* pillow
* requests
* opencv-python
