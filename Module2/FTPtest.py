#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:11:32 2017

@author: root
"""
#ips = ['ftp.uhulinux.hu','ftp.konkoly.hu','192.168.0.18','ftp.bme.hu',
#'ftp.debian.org','122.13.220.148','79.96.157.43',
#'ftp.hellug.gr','ftp.otenet.gr','ftp.linux.gr']

import ftplib
server = ftplib.FTP()
#server.connect('ftp.uhulinux.hu',21) done
#if(server.connect('ftp.konkoly.hu',21)):
#    server.login('anonymous','anon')
#    server.dir()
#else:
#    print "no connection"

server.connect('79.96.157.43',21)
server.login('anonymous','anon')
#server.connect('ftp.uhulinux.hu',21)
#server.connect('ftp.uhulinux.hu',21)
#server.connect('ftp.uhulinux.hu',21)
#server.connect('ftp.uhulinux.hu',21)
#server.connect('ftp.uhulinux.hu',21)
#server.connect('ftp.uhulinux.hu',21)


# For listing filenames only
#files = server.nlst()
#print files[0]
#for f in files:
#    print f
server.dir()
