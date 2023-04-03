import turtle
import math
def polygon(t,length,n):
    for i in range(n):
        t.fd(n)
        t.lt(length)
    
    
def circle(t,r):
    circum=math.pi*(2*r)  
    n=15
    length=circum/n
    polygon(t,length,n)
    
bob=turtle.Turtle()
t=bob
circle(bob,60)
 



