# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:32:18 2022

@author: ehima
"""

s='food '
count = 0
maxcount = 0
result = 0

for char in range(len(s) - 1):
    if (s[char] <= s[char + 1]):
        count += 1
        if count > maxcount:
            maxcount = count
            
            result = char + 1
        
    else:
        count = 0
startposition = result - maxcount
print('Longest substring in alphabetical order is:', s[startposition:result + 1])
