#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:29:49 2017

@author: root
"""

import mechanize

br = mechanize.Browser()

br.open('http://www.securitytube.net/video/3000')

for form in br.forms() :
    print form
    
br.select_form(nr=0) #selects the first form
br.form['q'] = 'defcon' #filling value q with defcon
br.submit() #submit the selected form

for link in br.links() :
    #print link #prints link objects
    """Link(base_url='http://www.securitytube.net/video/3000?q=defcon', 
    url='#', text='Megaprimers', tag='a', attrs=[('href', '#')])"""
    print link.url + " : " + str(link.text)