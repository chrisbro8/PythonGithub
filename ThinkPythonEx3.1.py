# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 02:36:20 2022

@author: ehima
"""

def right_justify(s):
    def length(s):
        return(len(s))
    calsword=70-length(s)
    space=(' '*calsword)+s
    print(space)
    return (len(space))
s=input('Enter a word:')
right_justify(s)