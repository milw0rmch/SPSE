#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:44:17 2017

@author: remnux
"""

fdesc = open("spse.txt","w")

for count in range(0,100):
    fdesc.write(str(count) + "\n")
    
fdesc.close()  
