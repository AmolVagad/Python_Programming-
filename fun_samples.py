# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:45:34 2017

@author: amol
"""
S = ['without','hello','bag','world']
items=[x for x in S.split(',')]
items.sort()
print (','.join(items))