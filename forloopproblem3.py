# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 03:22:58 2022

@author: ehima
"""

char='beggar'
newstring=""
for i in range(len(char)-1):
    if char[i]<=char[i+1]:
        newstring+=char[i]
        print(char[i])
    elif char[i]>char[i+1]:
        print('#'+char[i])
    else:
        print('*'+char[i])
print(i)
#print(newstring)
        
        