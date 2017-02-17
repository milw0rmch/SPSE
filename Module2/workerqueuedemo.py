#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:22:28 2017

@author: remnux
"""

import threading
import Queue
import time

#There should be a worker class which fetches task from this queue
#and executes them
#below is a subclass of threading.Thread

#https://docs.python.org/2/library/queue.html
#to be referred for queue functions
class WorkerThread(threading.Thread):
    
    def __init__(self, queue) : #consturctor takes the queue  from where the tasks will be fetched
                threading.Thread.__init__(self)
                self.queue = queue
                
    def run(self) :
        print "In Worker Thread"
        while True :
            counter = self.queue.get()
            print "Ordered to sleep for %d seconds!"%counter
            time.sleep(counter)
            print "Finished sleeping for %d seconds"%counter
            self.queue.task_done()
        
            
queue = Queue.Queue()

#creating the number of threads
for i in range(5) :
    print "Creating WorkerThread : %d"%i
    worker = WorkerThread(queue)
    worker.setDaemon(True)
    worker.start()
    print "WorkerThread %d Created"%i
    
#number of tasks    
for j in range(5) :
    queue.put(j)
    
queue.join() #wait for the task queue to be completely empty

print "All tasks are over!"