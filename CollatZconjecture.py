# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 22:33:10 2022

@author: ehima
"""

n=47
while n>1:
    
    if n%2==0:
        n=n/2
    elif n%2 or n%3 !=0:
        n=(3*n)+1
    print(n)
    