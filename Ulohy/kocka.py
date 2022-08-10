import turtle
import random
zofka=turtle.Turtle()
zofka.speed(10)
def stvorec(velkost):
    for i in range(4):
        zofka.forward(velkost)
        zofka.left(90)

def kocka():
    zofka.fillcolor('yellow')
    zofka.begin_fill()
    stvorec(20)
    zofka.left(90)
    zofka.forward(20)
    zofka.right(90)
    zofka.end_fill()
    strana1('blue')
    zofka.forward(-20)
    zofka.right(180)
    zofka.left(45)
    zofka.forward(10)
    zofka.left(-45)
    zofka.left(-90)

    strana2('red')
    zofka.left(90)
    zofka.forward(20)
    zofka.left(45)
    zofka.forward(10)
    zofka.left(135)

    zofka.right(90)
    zofka.forward(20)
    zofka.left(90)
    zofka.forward(20)

def strana1(farba):
    zofka.fillcolor(farba)
    zofka.left(45)
    zofka.begin_fill()
    zofka.forward(10)
    zofka.right(45)
    zofka.forward(20)
    zofka.right(135)
    zofka.forward(10)
    zofka.right(45)
    zofka.forward(20)
    zofka.end_fill()
def strana2(farba):

    zofka.fillcolor(farba)
    zofka.left(-45)
    zofka.begin_fill()
    zofka.forward(10)
    zofka.right(-45)
    zofka.forward(20)
    zofka.right(-135)
    zofka.forward(10)
    zofka.right(-45)
    zofka.forward(20)
    zofka.end_fill()


for i in range(8):
    kocka()
    zofka.right(45)


