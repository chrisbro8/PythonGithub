import turtle
import math
import time
def polygon(t,length,n):
    for i in range(n):
        angle=round(360/n,2)
        print(angle)
        t.fd(length)
        t.lt(angle)                                                                                                                                                       
bob=turtle.Turtle()
t=bob
polygon(bob ,100 ,7)
