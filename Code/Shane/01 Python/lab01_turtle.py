from turtle import *

def human():
    #from shane's lab01
    penup()

    goto(175,135)

    pendown()

    setheading(0)

    for i in range(180):
        forward (1)
        left(2)

    setheading(270)

    forward(15)

    setheading(0)

    forward(50)

    backward(50)

    setheading(180)

    forward(50)

    backward(50)

    setheading(270)

    forward (90)

    right(45)

    forward (90)

    backward(90)

    setheading(270)

    left(45)

    forward (90)

    backward(90)

human()

