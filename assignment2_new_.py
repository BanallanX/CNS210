#!/usr/bin/python


import urllib.request
import urllib
import os.path
import requests
import argparse
from bs4 import BeautifulSoup

print("Beginning download of Python - Input Date and Version")

req = requests.get('https://www.python.org/downloads/')
cont = req.content
soup = BeautifulSoup(cont, 'html.parser')
all_vers = soup.select('.download-list-widget, .list-row-container li')
print("Python: Date > Version")
userdateinput = input("Please Enter Date: - Month (or Mon. if over 5 letters) Day(NUM), Year(NUM) - :")
usr_dat = f'{userdateinput}'
print("Chosen Date:", usr_dat, "> Version")   
for the_ver in all_vers:
    for inp_ver in the_ver.select(".release-date"):        
        
#        print(inp_ver.get_text())
        if usr_dat in the_ver.select(".release-date")[0].get_text():
            print(usr_dat, str(the_ver.select(".release-number")[0].get_text()).split(" ")[1])
            date_list = (str(the_ver.select(".release-number")[0].get_text()).split(" ")[1])
       
#            print(date_list, the_ver.select(".release-date")[0].get_text())

#    print(link)
#        if "April 6, 2013" in link.select(".release-date")[0].get_text():               
#                date_version = [link.select(".release-date")[0].get_text()], [link.select(".release-number")[0].get_text().split(' ')[1]]
#                print(date_version)


#userdateinput = input("Please Enter Date: -Month Day(NUM), Year(NUM)- format:")
#usr_dat = f'{userdateinput}'
#print(usr_dat)


#        print(inp_ver)
        
#        continue
               

#for the_dat in all_vers:
#    for inp_dat in the_dat.select('.release-date'):
#        print(inp_dat)
#        print(the_dat.select('.release-date'))


#        continue 

#for usr_dat in the_dat.select('.release-date'):
#    print(usr_dat)
#    print([inp_ver.get_text().split(" ")[1]])
        

#if (the_ver) in all_vers:
#    print([inp_dat.get_text()], [inp_ver.get_text()])
 #       if "April 6, 2013" in link.select('.release-date').get_text():
 #           date_version = [link.select('.release-date')[0].get_text()], [link.select(".release-number")[0].get_text().split(' ')[1]]
 #       print (inp_ver.get_text())
        
#tagslis = soup('li')


value = input("Please Enter Version:") 

user_l = f"https://www.python.org/ftp/python/{value}/python-{value}.amd64.msi"
user_fil = f'ben-python-{value}.msi'

print('Download URL and File name', user_l, user_fil )

urllib.request.urlretrieve(user_l, user_fil)

print("Download Complete")