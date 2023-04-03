# -*- coding: utf-8 -*-
"""
Created on Wed May 25 04:38:20 2022

@author: ehima
"""
def mult_iter(a,b):
    result=0
    while b>0:
        result+=a
        b-=1
    
    return result
mult_iter(3,2)