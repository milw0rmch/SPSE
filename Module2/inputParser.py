#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 11:39:00 2017

@author: root
"""

def input_Parser(portRange):
    
    plist = portRange.split("-")
  #  print plist[0]
  #  print plist[1]
    
    portList = range(int(plist[0]),int(plist[1])+1)
    return portList
  #  print portList[2]
    
    #for i in portList:
     #   print str(i)
    
  ##  print "-"
    ##print portRange[1]
def print_Parser():
    
    plist = input_Parser("51-60")
    
    for i in plist:
        print(i)
        

print_Parser()
        