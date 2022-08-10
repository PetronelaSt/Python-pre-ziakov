import turtle


def tallyMarks(number):
    turtle.right(90)
    x = 0
    for i in range(1, number + 1):
        if i % 5 == 0:
            turtle.right(135)
            turtle.forward(30 * (2 ** (1 / 2)))
            turtle.right(225)
        else:
            turtle.penup()
            turtle.goto(x * 10, 0)
            turtle.pendown()
            turtle.forward(30)
        x = x + 1


def tallyMarks2(number):
    turtle.right(90)
    for i in range(1, number + 1):
        if i % 5 == 0:
            turtle.forward(15)
            turtle.right(90)
            turtle.pendown()
            turtle.forward(25)
            turtle.penup()
            turtle.forward(-35)
            turtle.right(90)
            turtle.forward(15)
            turtle.right(180)
        else:
            turtle.pendown()
            turtle.forward(30)
            turtle.forward(-30)
            turtle.penup()
            turtle.left(90)
            turtle.forward(5)
            turtle.right(90)


number = int(input("Číslo na prevod: "))
tallyMarks2(number)
