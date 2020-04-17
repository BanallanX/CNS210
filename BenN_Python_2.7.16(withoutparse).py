#!/usr/bin/python
import urllib
import os.path

print("Beginning download of Python 2.7.4 - Release Date: April 6, 2013")

urllib.urlretrieve('https://www.python.org/ftp/python/2.7.4/python-2.7.4.amd64.msi', 'ben-python2_7_4.msi')

print("Completed download")