import string
number=[1,2,3,4,5,6,7,8,9,0]
upalpha=list(string.ascii_uppercase)
loalpha=list(string.ascii_lowercase)
def check(a,sol=''):
    number='0123456789'
    for i in a:
        if i  in number:
            sol='true'
            break
        else:
            sol='false'
      

    return sol
def space(b,ans=''):
    if ' ' in password:
        ans='false'
    else:
        ans='true'
    return ans
def lettersUp(c,upans='false'):
    for i in c:
        if i in upalpha:
            upans='true'
            break
    return(upans)
def lettersDown(c,downans='false'):
    for i in c:
        if i in loalpha:
            downans='true'
            break
    return(downans)
            
        
print('your password should include uppercase,lowercase')
print('your password length should be greater than 8 and no spaces')
password=input('Enter a password:')
mycount=0
if len(password)<8:
    print('The length of the password is less than 8',end=',')
    mycount+=1

if check(password)=='false':
    print('no number in the password',end=',')
    mycount+=1
    
if space(password)=='false':
    print('there should be no space',end=',')
    mycount+=1
if lettersUp(password)=='false':
    print('You need uppercase ',end=',')
    mycount+=1
if lettersDown(password)=='false':
    print('You need lowercase',end=',')
    mycount+=1
if mycount>0  or mycount<1:
    if mycount>0:
        print('That password didnt meet all condition tryagain!')
    elif mycount<1:
        print('That password meet all condtion :) kudos')
