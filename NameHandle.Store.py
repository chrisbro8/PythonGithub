# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 02:37:26 2022

@author: ehima
"""

nameHandle=open('kids','w')
for i in range(2):
    name=input('Enter your names:')
    nameHandle.write(name + '\n')
nameHandle.close()