#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:48:07 2017

@author: root
"""

import sys
import time
import urllib

global rem_file 
global loc_file

rem_file = "ftp://ftp.ubuntu.com/ubuntu/ubuntu/dists/vivid/Contents-i386.gz"

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024*duration))
    percent = int(count*block_size*100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                     (percent, progress_size / (1024*1024),speed,duration)) 
    sys.stdout.flush()
    
urllib.urlretrieve(rem_file,"test",reporthook)

       