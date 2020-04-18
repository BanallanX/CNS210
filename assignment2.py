#!/usr/bin/python

#import urllib2
import urllib
import os.path
import requests
import argparse
from bs4 import BeautifulSoup

#parse = argparse.ArgumentParser()
#parse.add_argument('html', help="Add python release date and/or version")

#args = parser.parse_args()

#args.req

print("Beginning download of Python 2.7.4 - Release Date: April 6, 2013")

#urllib.urlretrieve('https://www.python.org/ftp/python/2.7.4/python-2.7.4.amd64.msi', 'ben-python-2_7_4.msi')



req = requests.get('https://www.python.org/downloads/')
#print(req.content)
#for line in req:
#    print(line.decode().strip())

soup = BeautifulSoup(req.content, 'html.parser')
#tags = soup('a')
#for tag in tags:
#    print(tag.get('href', None))

#ReDa = soup.find_all("release-date")
#for rd in ReDa:
#    print(rd.get('href', None))
tagslis = soup('li')
#for tagli in tagslis:
    #print(tagli.find('span', 'class'))
#print(tags.prettify())


for link in soup.select('.list-row-container li'):
#    print(link)
#    for data in link:
#        print(data.find_all('span'))
    
#    print(link.findAll('span'))
#    print(link.span)
#    print(link.select(".release-date"))
    print(link.select(".release-date")[0].get_text())
    
#    print(link.prettify())
print("Completed download")
