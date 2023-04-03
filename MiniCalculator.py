# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 00:23:49 2022

@author: ehima
"""
input1=(input('Enter the first value:'))
input2=(input('Enter the first value:'))
integer1=float(input1)
integer2=float(input2)
sign1='x'
sign2='+'
sign3='-'
sign4='/'
sign_user=input('Enter a sign:'+sign1+ sign2+ sign3+ sign4+'::::')
loweruser=sign_user.lower() #change the value of X to x incase of user capsl lock
if loweruser==sign1:
    print(integer1*integer2)
elif sign_user==sign2:
    print(integer1+integer2)
elif sign_user==sign3:
    print(integer1-integer2)
elif sign_user==sign4:
    if integer2<=0:
        print('''error,cant divide a value by 0''')
    else:
        print(integer1/integer2)
    
