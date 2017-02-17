#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 13:23:33 2017

@author: remnux
"""

##else clause is only executed when your while condition becomes false. 
##If you break out of the loop, or if an exception is raised, it wont be executed

count = 0;
while count < 5:
    print count, "is less than 5"
    count+=1
else:
    print count, " is not less than 5"
    