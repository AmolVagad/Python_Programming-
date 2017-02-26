# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:06:18 2017

@author: amol
"""
import Functions_1

list = [1,9,7,6,5,48,3,1,52,5,57]
for i in list:
    if i % 2 == 0:
        print('Prime=',i)
    else:
        print('Not prime=',i)
        
        
for num in range(len(list)-1, 0,-1):
    for i in range(num):
        
        if list[i] > list[i+1]:
            temp =list[i]
            list[i]=list[i+1]
            list[i+1] =temp
print('The sorted list is = ', list)

y=Functions_1.inr_to_usd(9000)
print(y)