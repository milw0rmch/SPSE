#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 14:36:49 2017

@author: root
"""

x=range(1,25)

chunk = len(x)/6

l=[]
i=0
while i<len(x):
    if len(l)<=4:
        l.append(x[i:i+chunk])
    else:
        l.append(x[i:])
        break
    i+=chunk
    
print l[0]