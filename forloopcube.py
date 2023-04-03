# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 02:46:09 2022

@author: ehima
"""

cube=8
for guess in range (abs(cube+1)):
    if guess**3>=(abs(cube)):
        break
if guess**3!=abs(cube):
    print(str(cube)+"Is not a perfect cube")
else:
    if cube<0:
        guess=-guess
print("cube root of "+str(cube)+"is"+str(guess))