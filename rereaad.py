# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 04:09:58 2022

@author: ehima
"""
s="mabrmopt"
char=charc=s[0]
for i in range(1,len(s)): 
    if s[i-1] <= s[i]:
     char+=s[i]
     if len(char)>len(charc):
      charc=char
    else:
     char=s[i]
print('Longest substring in alphabetical order is: '+charc) 
