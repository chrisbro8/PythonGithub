def print_n(s,n):
    if n<=0:
        return
    else:
        print(s)
        print_n(s,n-1)

        
def do_n(s=print_n,n):
    return(s,n)
print_n(s='hello',n=3)
do_n(s=print_n,n=3)w