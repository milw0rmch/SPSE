#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:32:50 2017

@author: remnux
"""
import os,sys

def get_usb_messages(): 
    search_str='usb'

    fdesc=open("/var/log/syslog.1","r")

    for line in fdesc.readlines():
        if search_str in line:
            print line
        
    fdesc.close()
    
if __name__ == "__main__":
    get_usb_messages()