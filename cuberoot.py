x=int(input("enter an Interger"))
ans=0
while ans**3 < =x:
    ans=ans+1
if ans**3!=x:
print("The value provided is not a perfect cube")
else:
    print('The cube root of'+str(x)+ 'is' +str(ans)))