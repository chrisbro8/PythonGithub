# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 02:19:01 2022

@author: ehima
"""

def add_binary(a,b):
    sum=a+b
    result=''
    while sum>=0:
        result=str(sum%2)+result
        sum=sum//2
    return sum
add_binary(5,9)