# -*- coding: utf-8 -*-
"""
Created on Wed May 25 04:37:28 2022

@author: ehima
"""

x=1567
n=2
while n<x:
    if x%n==0:
        print(n)
        x=x//n
        n=n-1
    n=n+1
print(n)
        