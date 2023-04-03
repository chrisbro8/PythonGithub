import math
def polysum(n,s):
    x=math.tan(math.pi/n)
    area=0.25*n*(s**2)/x
    peri=(n*s)
    Asum=area+peri**2
    return round(Asum,4)