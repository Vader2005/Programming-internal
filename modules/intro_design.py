from turtle import *
from time import sleep

def application():
    # Create the variables

    bgcolor("black") #sets the background color of the window
    z = [Turtle(), Turtle()] #Create the turtle objects
    x = 6
    colors = ["red", "yellow", "blue", "lime"]

    # For loops
    for index, i in enumerate(z):
        i.speed(10)
        i.color("white")
        i.shape("circle")
        i.shapesize(0.3)
        i.width(3)
        i.pu()
        i.seth(90)
        i.fd(350)
        i.seth(-180)
        i.pd()
    z[0].pu()

    delay(0)
    speed(0)
    ht()
    sleep(4)

    # Iterate the different colors

    for i in colors:
        color(i)
        for i in range(360):
            z[0].fd(x)
            z[0].lt(1)
            pu()
            goto(z[0].pos())
            pd()
            z[1].fd(2*x)
            z[1].lt(2)
            goto(z[1].pos())
    #z.bye()
    from First_window import Window
    Window() # Load the first gui window

application()
