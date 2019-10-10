# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:39:41 2017

@author: ishort
"""

""" Does not work - module thread deprecated??"""

import thread
import time

#Define a function for the thread
def print_time(threadName, delay):
    
    count = 0
    
    while(count < 5):
        
        time.sleep(delay)
        count += 1
        
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        
try:
    
    thread.start_new_thread(print_time("Thread-1", 2))
    thread.start_new_thread(print_time("Thread-2", 4))
    
except:
    
    print("Error: Unable to start thread")
    
while 1:
    
    pass


        
