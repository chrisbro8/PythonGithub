# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 01:36:03 2022

@author: ehima
"""

import math
minimumMonthlyPayment=10
i=1
x=balance
while balance>0:
    i+=1
    if i==13:
        balance=x
        minimumMonthlyPayment+=10
        i=0
    else:
        monthlyinterestRate=(annualInterestRate/12.0)
        monthlyunpaidBalance=balance-minimumMonthlyPayment
        unpaidBalance=monthlyunpaidBalance+(monthlyunpaidBalance*monthlyinterestRate)
        balance=unpaidBalance
print("Lowest Payment:"+' '+str(minimumMonthlyPayment))