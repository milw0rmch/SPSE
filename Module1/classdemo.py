#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 13:56:07 2017

@author: remnux
"""

class Calculator:
    
    ##define constructor of the class
    def __init__(self, ina, inb):
        self.a = ina
        self.b = inb
        
    def add(self):
        return self.a + self.b
    
    def mul(self):
        return self.a*self.b
    
    
newCalculation = Calculator(10,20)

print 'a+b: %d'%newCalculation.add()
print 'a*b: %d'%newCalculation.mul()


