# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 08:13:15 2017

@author: amol
"""

class Calculator:
    a = 7
    b = 5
    result1 = 0
    result2 = 0
    def Sum(self):
        self.result1 = self.a + self.b
        self.a += 1
        print('The sum =', self.result1)
       
    def Diff(self):
         self.result2 = self.a - self.b
         print('The diff =', self.result2)
         
Cal1 = Calculator()
Cal1.Sum()
Cal1.Sum()
Cal1.Diff()
Cal1.Diff()
    