# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 02:24:45 2022

@author: ehima
"""

def gcditer(a,b):
    testvalue=min(a,b)
    while a%testvalue!=0 or b%testvalue!=0:
        testvalue-=1
    return testvalue
gcditer(9,21)