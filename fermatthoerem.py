def checkfermat(a,b,c,n):
    sumuser=(a**n) + (b**n)
    if n<=2:
        print("you have to make n hgher than 2")

    else:
        if  sumuser==c**n:
            print('holy smokes fermat was wrong')
        else:
            print('No that doesnt work,dont think it can be  broken :)')
def promptuser():
    a=int(input("Enter a value for a:"))
    b=int(input("Enter a value for b:"))
    c=int(input("Enter a value for c:"))
    n=int(input("Enter a value for n:"))
    return checkfermat(a,b,c,n)
promptuser()