# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:55:45 2017

@author: amol
"""

def sq_nos(n):
    for i in n:
        yield(i*i)
        
my = sq_nos([1,5,6])
print(list(my))
''' List cmp'''

my_nums= [x*x for x in [1,5,7]]
print(list(my_nums))