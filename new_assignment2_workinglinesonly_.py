#!/usr/bin/python

import urllib.request
import urllib
import os.path
import requests
import argparse
from bs4 import BeautifulSoup

print("Beginning Download of Python - Input Date and Version")

req = requests.get('https://www.python.org/downloads/')
cont = req.content
soup = BeautifulSoup(cont, 'html.parser')
all_vers = soup.select('.download-list-widget, .list-row-container li')
print("Python: Date > Version")
userdateinput = input("Please Enter Date: - Month (or Mon. if over 5 letters) Day(NUM), Year(NUM) - : ")
usr_dat = f'{userdateinput}'
print("Chosen Date:", usr_dat, "> Version")   
for the_ver in all_vers:
    for inp_ver in the_ver.select(".release-date"):        
        
        if usr_dat in the_ver.select(".release-date")[0].get_text():
            print(usr_dat, str(the_ver.select(".release-number")[0].get_text()).split(" ")[1])
            date_list = (str(the_ver.select(".release-number")[0].get_text()).split(" ")[1])
       
value = input("Please Enter Version: ") 

user_l = f"https://www.python.org/ftp/python/{value}/python-{value}.amd64.msi"
user_fil = f'ben-python-{value}.msi'

print('Download URL and File name', user_l, user_fil )

urllib.request.urlretrieve(user_l, user_fil)

print("Download Complete")