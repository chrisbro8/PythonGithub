# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 02:06:51 2022

@author: ehima
"""
s='boysboyiy'
cout=0
les=len(s)-2
for i in range(les):
    z=s[i:i+3]
    if z=="boy":
        cout+=1
    print(z)
print(cout)
    