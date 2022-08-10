import turtle
import random


def flower(size, num, distance):
    turtle.colormode(255)
    turtle.goto(0, size)
    turtle.color(
        random.randrange(0, 257, 10),
        random.randrange(0, 257, 10),
        random.randrange(0, 257, 10),
    )
    for i in range(num):
        turtle.forward(distance)
        turtle.right(90)
        turtle.begin_fill()
        # dá sa aj pomocou shape("circle")
        turtle.circle(size)
        turtle.end_fill()
        turtle.goto(0, size)
        turtle.right(360 / num - 90)
    turtle.color(
        random.randrange(0, 257, 10),
        random.randrange(0, 257, 10),
        random.randrange(0, 257, 10),
    )
    turtle.goto(0, 0)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.hideturtle()


flower(
    int(input("Zadajte veľkosť lupeňov: ")),
    int(input("Zadajte počet lupeňov: ")),
    int(input("Zadajte vzdialenosť od stredu: ")),
)
