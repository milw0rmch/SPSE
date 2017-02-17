#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 08:53:47 2017

@author: root
"""
import threading
import Queue
import time
import ftplib

server = ftplib.FTP()
ips = ['ftp.uhulinux.hu','ftp.konkoly.hu','192.168.0.18','ftp.bme.hu',
'ftp.debian.org','122.13.220.148','79.96.157.43',
'ftp.hellug.gr','ftp.otenet.gr','ftp.linux.gr']
queue = Queue.Queue()

for i in ips:
    queue.put(i)

class WorkerThread(threading.Thread):
    
    def __init__(self, queue) : #consturctor takes the queue  from where the tasks will be fetched
                threading.Thread.__init__(self)
                self.queue = queue
                
    def run(self) :
        #while not self.queue.empty():
        while True:
            ip = self.queue.get()
            print ip + '\n'
            server.connect(ip,21)
            server.login('anonymous','anon')
            server.dir()
            server.close()
            #print ip
            self.queue.task_done()
        
        
for i in range(5) :
    #print "Creating WorkerThread : %d"%i
    worker = WorkerThread(queue)
    worker.setDaemon(True)
    worker.start()
    #print "WorkerThread %d Created"%i

queue.join() #wait for the task queue to be completely empty

print "All tasks are over!"
        