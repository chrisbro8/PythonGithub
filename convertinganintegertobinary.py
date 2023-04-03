# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 03:22:54 2022

@author: ehima
"""
num=19
result=''
while num>0:
    result =str(num%2)+result
    num=num//2
print(result)

