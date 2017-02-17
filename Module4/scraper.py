#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 12:09:45 2017

@author: root
"""

import urllib
import bs4
from bs4 import BeautifulSoup

httpResponse = urllib.urlopen('http://www.securitytube.net/video/3000')

html = httpResponse.read()

bs = BeautifulSoup(html,"lxml")

descr = bs.find('div', id="left") #<div id="description">
#print descr

videoLink= bs.find('iframe', {'title' : 'YouTube video player'})

print videoLink['src']