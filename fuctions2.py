# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 04:38:58 2022

@author: ehima
"""

def printName(firstName,lastName,reverse = False):
    if reverse:
        print(lastName+' '+firstName)
    else:
        print(firstName,lastName)
printName('Ehimare','Brownwell')
printName('Ehimare','Brownwell',True)