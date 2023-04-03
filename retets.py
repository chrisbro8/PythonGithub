import turtle
def square(bob,length):
    for i in range(length):
        bob.fd(length)
        bob.lt(90)
    return
square(bob=turtle.Turtle(),4)
turtle.mainloop