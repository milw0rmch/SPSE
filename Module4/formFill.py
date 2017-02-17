#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 15:08:39 2017

@author: root
"""

import mechanize

br = mechanize.Browser()

br.open('http://www.securitytube.net/video/3000')

for form in br.forms() :
    print form

