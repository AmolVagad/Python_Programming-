# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 09:06:42 2017

@author: amol
"""

class Flash():
    
    def run(self):
        print('running')
        
    def fight(self):
        print('fighting')
        
class Zoom():
    
    def beat(self):
        print('Beats Zoom')
        
        
class Iris():
    
    def saves(self):
        print('Saves Iris')
        
class Kid_Flash(Flash, Zoom, Iris):
    pass

Speed = Kid_Flash()
Speed.beat()
Speed.fight()
Speed.run()
Speed.saves()

