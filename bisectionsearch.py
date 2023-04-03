# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 01:23:48 2022

@author: ehima
"""

epsilon=0.01
x=25
low=0.0
high=x
ans=(low+high) /2
numofguess=0.0
while abs(ans**2-x)>=epsilon:
    print('low'   + str(low)+  'high'+str(high)+  'ans'+   str(ans))
    numofguess+=1
   
    if ans**2<x:
        low=ans
    else:
        high=ans
    ans=(low+high)/2
print(numofguess)