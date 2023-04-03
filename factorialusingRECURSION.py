# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 22:06:30 2022

@author: ehima
"""

def fact(n):
    if n==1:
        return 1
    else:
        return n *fact(n-1)
print(fact(4))