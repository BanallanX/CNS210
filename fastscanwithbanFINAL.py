#!/usr/bin/python

import os
import re
from datetime import datetime
import socket
import time
import threading
from queue import Queue



print_lock = threading.Lock() 

usrtarg = input("Please Enter Target: ")
target = f'{usrtarg}'
print("Your Target Is: ",target)

usrport1 = input("Please Enter Starting Port: ")
targport1 = f'{usrport1}'

usrport2 = input("Please Enter Ending Port: ")
targport2 = f'{usrport2}'

print("Port Range Selected: ", usrport1, "-", usrport2)

def ban(target, xport):
    bannergrabber = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
    bannergrabber.settimeout(1)     
    try:
        bannergrabber.connect((target, xport))
        bannergrabber.send(b"GET / \r\n")
        banner = str(bannergrabber.recv(4096), 'ascii')
        bannergrabber.close()
        print (str(banner), "\n")
    except: 
        print ("Cannot connect to port ", xport)


def portscan(xport):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn = soc.connect((target, xport))

        with print_lock:
            print('Port', xport, 'is open!')
            ban(target, xport)

        conn.close()    
    except:
        pass

start = time.time()
def threader():
    while True:
        pnum = q.get()
        portscan(pnum)
        q.task_done()
q = Queue()
for x in range(50):
    thr = threading.Thread(target=threader)
    thr.daemon = True
    thr.start()
for pnum in range(int(targport1), int(int(targport2) + 1)):
    q.put(pnum)
q.join()
print("Completed In: ", time.time()-start, "Seconds")
   