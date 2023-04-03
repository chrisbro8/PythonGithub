# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 02:25:23 2022

@author: ehima
"""

def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1) +fib(x-2)
fib(5)