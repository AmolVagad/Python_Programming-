# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:46:24 2017

@author: amol
"""
result =[]
def sq_nos(n):
    for i in n:
        result.append(i*i)
    return result
        
my_nums = sq_nos([1,2,3])
print(my_nums)



def inr_to_usd(cash):
    USD = cash/67
    return USD 
    
inr_to_usd(40000)