# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 01:06:40 2022

@author: ehima
"""

def isPalindrome(s):
    def toChars(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans= ans + c
        return ans 
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] ==s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))
print("")
print('Is eve a palindrome?')
print(isPalindrome("folof"))