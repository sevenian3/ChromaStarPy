# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:51:49 2017

@author: ishort
"""

import threading
import time

exitFlag = 0

class MyThread(threading.Thread):
    
    def __init__(self, threadID, name, counter):
        
        threading.Thread.__init__(self)
        
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        
        print("Starting " + self.name)
        print_time(self.name, self.counter, 2)
        print("Exiting " + self.name)
        
def print_time(threadName, counter, delay):
        
    while(counter):
            
        if (exitFlag):
            threadName.exit()
                
        time.sleep(delay)
            
        print ("%s: %s" % (threadName, time.ctime(time.time())))
            
        counter -= 1
            
#create new threads
thread1 = MyThread(1, "Thread-1", 2)
thread2 = MyThread(2, "Thread-2", 4)

#start new threads
thread1.start()
thread2.start()

print("Exiting main thread")


                
        
        
            
        
        