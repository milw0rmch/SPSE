#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 07:44:23 2017

@author: remnux
"""

import thread
import time

#this defines the task to perfomr in the threads
def worker_thread(id) :
    
    print "Thread ID %d now alive!"%id
    count = 0
    while count < 5 :
        print "Thread with ID %d has counter value %d"% (id,count)
        time.sleep(2)
        count+=1        

#This initiates the number of threads required to do the task
for i in range(5) :
    #start new thread takes the function name and values to input as a tuple
    thread.start_new_thread(worker_thread, (i,)) 

print "Main thread going for a infinite wait loop"

while True :
    pass           