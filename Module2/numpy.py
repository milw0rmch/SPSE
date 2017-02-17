#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 14:47:59 2017

@author: root
"""

import numpy

x = numpy.arange(25)

l=numpy.array_split(x,3)

print l[0]