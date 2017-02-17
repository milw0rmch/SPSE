#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:55:27 2017

@author: remnux
"""

fdesc=open("spse.txt","r")

for line in fdesc.readlines() :
    print line.strip()
    
fdesc.close()