# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 08:32:42 2017

@author: amol
"""

class Addon:
    a = 5
    res = 0
    def __init__(self, x,y):
        self.res = x + y
        
    def get_result(self):
        print(self.res)
        
        
Sum1 = Addon(20,50)
Sum1.get_result()

Sum2 = Addon(220,20)
Sum2.get_result()
