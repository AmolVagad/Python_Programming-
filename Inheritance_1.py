# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 08:50:54 2017

@author: amol
"""

class Super():
    
    def hero_name(self):
        print('Batman')
        
class Real(Super):
    
    def real_name(self):
        print('Bruce Wayne')
        
    def hero_name(self):
        print('Wonder Woman')
        
Batsy = Real()
Batsy.hero_name()
Batsy.real_name()
