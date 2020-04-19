#!/usr/bin/python

#import urllib2
import urllib.request
import os.path
import requests
import argparse
from bs4 import BeautifulSoup

#parse = argparse.ArgumentParser()
#parse.add_argument('html', help="Add python release date and/or version")

#args = parser.parse_args()

#args.req

print("Beginning download of Python - Release Date: April 6, 2013 - Choose Version")

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
#    print(link.select(".release-date")[0].get_text())
    
    if "April 6, 2013" in link.select(".release-date")[0].get_text(): 
        date_version = [link.select(".release-date")[0].get_text()], [link.select(".release-number")[0].get_text().split(' ')[1]]
        print(date_version)
        
    
value = input("Please Enter Version:") 

user_l = f"https://www.python.org/ftp/python/{value}/python-{value}.amd64.msi"
user_fil = f'ben-python-{value}.msi'

#user_ver = input("what version?")
#val = "https://python.org/ftp/python/" + user_ver + "/python-" + user_ver + ".amd.64.msi", "ben-python- " + user_ver
#print(val)
#urllib.request.urlretrieve("https://python.org/ftp/python/" + user_ver + "/python-" + user_ver + ".amd.64.msi", "ben-python- " + user_ver)
print('Download URL and File name', user_l, user_fil )
urllib.request.urlretrieve(user_l, user_fil)


#urllib.urlretrieve('"https://www.python.org/ftp/python/" + {value} + "/python-" + {value} + ".amd64.msi", "ben-python-"+ {value}')

#https://www.python.org/ftp/python/2.7.4/python-2.7.4.amd64.msi
#https://www.python.org/ftp/python/3.3.1/python-3.3.1.amd64.msi
#https://www.python.org/ftp/python/3.2.4/python-3.2.4.amd64.msi

#    print(link.prettify())
#   print(link.select(".release-date")[0].get_text())
#    if "April 6, 2013" in link.select(".release-date")[0].get_text():

#       print(link.select(".release-number")[0].get_text().split(' ')[1])







print("Completed download")






