#!/usr/bin/python


import urllib.request
import os.path
import requests
import argparse
from bs4 import BeautifulSoup

print("Beginning download of Python - Release Date: April 6, 2013 - Choose Version")

req = requests.get('https://www.python.org/downloads/')
soup = BeautifulSoup(req.content, 'html.parser')
tagslis = soup('li')

for link in soup.select('.list-row-container li'):
        if "April 6, 2013" in link.select(".release-date")[0].get_text():               
                date_version = [link.select(".release-date")[0].get_text()], [link.select(".release-number")[0].get_text().split(' ')[1]]
                print(date_version)
        
value = input("Please Enter Version:") 

user_l = f"https://www.python.org/ftp/python/{value}/python-{value}.amd64.msi"
user_fil = f'ben-python-{value}.msi'

print('Download URL and File name', user_l, user_fil )

urllib.request.urlretrieve(user_l, user_fil)

print("Completed download")