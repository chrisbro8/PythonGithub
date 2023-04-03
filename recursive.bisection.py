# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 21:28:32 2022

@author: ehima
"""

def isIn(astr,char):
    midlength=len(astr)//2
    midchar=astr[midlength]
    if astr=='':
        return False
    if len(astr)==1:
        return astr==char
    if midchar==char:
        return True
    elif char>midchar:
        return isIn(astr[midlength+1:],char)
    else:
        return isIn(astr[:midlength],char)
isIn('beforst','t')
isIn('beforst','f')