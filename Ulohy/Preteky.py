from turtle import *

# vytvorenie prvej korytnacky
blueTurtle = Turtle()
blueTurtle.shape("turtle")
blueTurtle.color("blue")

# vytvorenie druhej korytnacky
redTurtle = Turtle()
redTurtle.shape("turtle")
redTurtle.color("red")

# posun korytnačiek
# blueTurtle.forward(20)
# redTurtle.forward(-20)


# domcek
def house(size):
    blueTurtle.begin_fill()
    for i in range(4):
        blueTurtle.forward(size)
        blueTurtle.right(90)
    blueTurtle.end_fill()

    redTurtle.left(60)
    redTurtle.begin_fill()
    for i in range(3):
        redTurtle.forward(size)
        redTurtle.right(120)
    redTurtle.end_fill()


def circles(sizeMax, sizeMin):
    blueTurtle.circle(sizeMax)
    blueTurtle.right(180)
    blueTurtle.circle(sizeMin)

    redTurtle.circle(sizeMin)
    redTurtle.right(180)
    redTurtle.circle(sizeMax)


# polovica kruhu cervena, polovica zlta
def colorCircle(size):
    blueTurtle.begin_fill()
    blueTurtle.circle(size, 180)
    blueTurtle.end_fill()

    redTurtle.begin_fill()
    redTurtle.circle(size, -180)
    redTurtle.end_fill()


# hviezda
def star(size):
    redTurtle.right(360 / 20)
    for i in range(10):
        blueTurtle.forward(size)
        blueTurtle.forward(-size)
        blueTurtle.right(360 / 10)

        redTurtle.forward(size)
        redTurtle.forward(-size)
        redTurtle.right(360 / 10)


# klasicky kvet
def flower(size):
    redTurtle.begin_fill()
    for i in range(5):
        redTurtle.circle(size)
        redTurtle.right(360 / 5)
    redTurtle.end_fill()

    blueTurtle.goto(0, -size)
    blueTurtle.begin_fill()
    blueTurtle.circle(size)
    blueTurtle.end_fill()


def flower2(size):
    redTurtle.left(360 / 10)

    blueTurtle.begin_fill()
    redTurtle.begin_fill()
    for i in range(5):
        blueTurtle.circle(size)
        blueTurtle.left(360 / 5)

        redTurtle.circle(size - size / 3)
        redTurtle.left(360 / 5)
    blueTurtle.end_fill()
    redTurtle.end_fill()


# house(120)
# circles(60, 45)
# colorCircle(70)
# star(80)
# flower(50)
# flower2(60)

# redTurtle.hideturtle()
# blueTurtle.hideturtle()
