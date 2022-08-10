import turtle
import random


def target(numberOfCircles, space):
    turtle.colormode(255)
    turtle.penup()
    turtle.goto(0, float(space * numberOfCircles) * (-1.0))
    for i in range(0, numberOfCircles):
        turtle.pendown()
        turtle.color(
            random.randrange(0, 257, 10),
            random.randrange(0, 257, 10),
            random.randrange(0, 257, 10),
        )
        turtle.begin_fill()
        turtle.circle((space * numberOfCircles) - (i * space))
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(space)
        turtle.right(90)


target(int(input("pocet: ")), int(input("medzery: ")))
