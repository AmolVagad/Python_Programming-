# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:58:37 2017

@author: amol
"""

import random 

heads = 0;
tails = 0;


for x in range(0,100):
    flip = random.randint(0,1)
 
    
    if flip == 0:
        heads += 1
    else:
        tails += 1
        
print('Heads = %i.' %heads)
print('Tails = %i.' %tails)


