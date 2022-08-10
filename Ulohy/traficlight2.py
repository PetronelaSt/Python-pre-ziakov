import turtle


def drawLights(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    # prípadne cez shape("circle")
    turtle.circle(15)
    turtle.end_fill()


def drawBox():
    turtle.penup()
    turtle.goto(-30, 60)
    turtle.pendown()
    for i in range(0, 2):
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(120)
        turtle.right(90)
    turtle.right(90)
    drawLights(-15, 40, "grey")
    drawLights(-15, 0, "grey")
    drawLights(-15, -40, "grey")


drawBox()
turtle.hideturtle()
while True:
    drawLights(-15, 40, "red")
    drawLights(-15, 40, "grey")
    drawLights(-15, 0, "orange")
    drawLights(-15, 0, "grey")
    drawLights(-15, -40, "green")
    drawLights(-15, -40, "grey")
    drawLights(-15, 0, "orange")
    drawLights(-15, 0, "grey")
