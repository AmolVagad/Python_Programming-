# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 00:54:43 2017

@author: amol
"""

my_list = {1,2,3,4,5,6,7}
squares = [n*n for n in my_list]
print(squares)
primes = [n % 2!=0 for n in my_list]
print (primes) 