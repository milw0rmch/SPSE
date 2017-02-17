#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:23:21 2017

@author: remnux
"""

import socket

#sock_stream is for TCP
tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#to reuse same address after a server crash
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#bind socket to a port
tcpSocket.bind(("0.0.0.0",8000))
#open for listening,2 is the number of concurrent clients the socket can handle
tcpSocket.listen(2)

#client variable is the client socket trying to connect to us
print "Waiting for a client to connect"
(client, (ip,port)) = tcpSocket.accept()

print "Received connection from : ", ip

print "Starting ECHO output .... "

data = 'dummy'

while len(data) :
    data = client.recv(5)
    print "Client sent:   ",data
    client.send(data)
    

print "Closing connection ..."
client.close()

print "Shutting down server ..."
tcpSocket.close()