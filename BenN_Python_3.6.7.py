#!/usr/bin/python

#import urllib2
import urllib
import os.path
import requests
#import argparse
from bs4 import BeautifulSoup

#parse = argparse.ArgumentParser()
#parse.add_argument(help="Add python release date and/or version")

#args = parser.parse_args()

#args.pip
print("Beginning download of Python 2.7.4 - Release Date: April 6, 2013")

urllib.urlretrieve('https://www.python.org/ftp/python/2.7.4/python-2.7.4.amd64.msi', 'ben-python-2_7_4.msi')

print("Completed download")

req = requests.get('https://www.python.org/downloads/')
print(req.content)
#for line in request:
#    print(line.decode().strip())

soup = BeautifulSoup(req.content, 'html.parser')
#for link in soup.select('.list-row-container li')

