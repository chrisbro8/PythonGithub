# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 23:39:17 2022

@author: ehima
"""

def recur(base,exp):
    if exp==1:
        return base
    else:
        return base*recur(base,exp-1)
recur(2,3)