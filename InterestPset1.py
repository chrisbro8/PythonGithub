import math
for i in range(12):
        monthlyinterestRate=(annualInterestRate/12.0)
        minimumMonthlyPayment=monthlyPaymentRate*balance
        monthlyunpaidBalance=balance-minimumMonthlyPayment
        unpaidBalance=monthlyunpaidBalance+(monthlyunpaidBalance*monthlyinterestRate)
        balance=unpaidBalance
        rround=round(balance,2)
print("Expected Remaining balance:"+''+str(rround))