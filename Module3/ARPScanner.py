#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:52:45 2017

@author: root
"""

import scapy
import scapy.all
from scapy.all import srp,srp1,Ether,ARP,conf


for lsb in range(1, 50) :
    ip = "192.168.0." + str(lsb)
    arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst = "ff:ff:ff:ff:ff:ff")
    arpResponse = srp1(arpRequest,timeout=1,verbose=0)
    if arpResponse :
        print "IP: " + arpResponse.psrc + " MAC: " + arpResponse.hwsrc
    else:
        print "fail"