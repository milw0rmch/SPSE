#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:11:21 2017

@author: remnux
"""

import SocketServer
import SimpleHTTPServer

class HttpRequestHandler (SimpleHTTPServer.SimpleHTTPRequestHandler) :
    
    #do_GET is a method that can be overriden to take actions on certain 
    #scenarios for example custom message on admin page access
    def do_GET(self) :
        
        if self.path == '/admin' :
            #wfile is used to write to the client
            self.wfile.write('This page is only for Admins!')
            self.wfile.write(self.headers)
            
        else :
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        



httpServer = SocketServer.TCPServer(("",10000),HttpRequestHandler)
httpServer.serve_forever()