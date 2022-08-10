import turtle
from random import randint


def drawStar(size):
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(size)
        turtle.left(145)
    turtle.end_fill()


def drawNighSky(size, num):
    window = turtle.Screen()
    turtle.bgcolor("black")
    turtle.color("yellow")
    turtle.speed(0)
    for i in range(0, num):
        x = randint(-250, 250)
        y = randint(-250, 250)
        drawStar(size)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()


drawNighSky(int(input("Zadaj veľkosť hviezdy: ")), int(input("Zadaj počet hviezd: ")))


