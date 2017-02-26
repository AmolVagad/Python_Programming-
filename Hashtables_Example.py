# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 00:01:45 2017

@author: amol
"""

table = [None]*10;
def hash_fun(x):
    return x % 10
    
def insert(table, key, value):
    table[hash_fun(key)] = value 
    
insert(table, 118, 'cat')

table = [ [] for _ in range(10)]

insert(table, 118, 'dog')


insert(table, 118, 'cat')
print(table) 