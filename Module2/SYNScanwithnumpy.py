#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 14:56:17 2017

@author: root
"""

#x = numpy.arange(25)
#l=numpy.array_split(x,3)
#print l[0]

import thread
import time
import sys
import scapy
import scapy.all
from scapy.all import sr,sr1,srp,srp1,Ether,ARP,conf,IP,TCP
from scapy.volatile import RandShort
import numpy



def get_portList(portRange):
    plist = portRange.split("-")
    x = numpy.arange(int(plist[0]),int(plist[1])+1)
    global portList 
    portList = numpy.array_split(x,5)
    return portList

def port_range(portRange):
    l = get_portList(portRange)
    global A
    A=l[0]
    global B
    B=l[1]
    global C
    C=l[2]
    global D
    D=l[3]
    global E
    E=l[4]

def ports_scan(dst_ip,portRange):
    
    for i in portRange:
        print(i)
        dst_port = i    
        src_port = RandShort()  
        tcp_resp = sr1(IP(dst = dst_ip)/TCP(sport=src_port,dport=dst_port,
                   flags="S"),timeout=10,verbose=False)
        if(tcp_resp.getlayer(TCP).flags == 0x12):
            print "Port: " + str(dst_port) +" is open"


#try: 
 #   thread.start_new_thread(port_scan,("192.168.0.18",80,))
port_range("79-89")
try:
    thread.start_new_thread(ports_scan,("192.168.0.18",A,))
    thread.start_new_thread(ports_scan,("192.168.0.18",B,))
    thread.start_new_thread(ports_scan,("192.168.0.18",C,))
    thread.start_new_thread(ports_scan,("192.168.0.18",D,))
    thread.start_new_thread(ports_scan,("192.168.0.18",E,))
except:
    print "Error: unable to start thread"
    
while 1:
    pass