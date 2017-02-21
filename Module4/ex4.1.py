#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 11:29:11 2017

@author: root
"""

import sys
import time
import urllib

global rem_file 
global loc_file

rem_file = "ftp://ftp.ubuntu.com/ubuntu/ubuntu/dists/vivid/Contents-i386.gz"


def dlProgress(count,blockSize,totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r" + rem_file + "...%d%%" % percent )
    sys.stdout.flush()
    
    
sys.stdout.write(rem_file + "...")
urllib.urlretrieve(rem_file,"test",reporthook=dlProgress)

    
    