#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 10:11:44 2017

@author: root
"""

import thread
import time
import sys
import scapy
import scapy.all
from scapy.all import sr,sr1,srp,srp1,Ether,ARP,conf,IP,TCP
from scapy.volatile import RandShort

def port_scan(dst_ip,dst_port):
    src_port = RandShort()
    
    tcp_resp = sr1(IP(dst = dst_ip)/TCP(sport=src_port,dport=dst_port,
                   flags="S"),timeout=10)
    if(tcp_resp.getlayer(TCP).flags == 0x12):
        print "Port: " + str(dst_port) +" is open"
        

try: 
    thread.start_new_thread(port_scan,("192.168.0.18",80,))
#port_scan("192.168.0.18",80)
except: 
    print "Error: unable to start thread"
    
while 1:
    pass