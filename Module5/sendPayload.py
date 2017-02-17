#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:19:38 2017

@author: root
"""

import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((sys.argv[1],10000))

buffer = "A" * 500

sock.send(buffer)

print sock.recv(1024)

sock.close()
