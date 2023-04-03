# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 01:05:16 2022

@author: ehima
"""

n=input('Give me a number over 100::')
try :
    n=int(n)
    if n<100:
        print(n,'is not over 100')
    else:
        print(n,'is over 100')
except ValueError:
    print('requires a valid integer')
    
    
    