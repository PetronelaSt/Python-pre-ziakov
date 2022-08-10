import turtle, random

def drawPicture():
    turtle.goto(-300,100)
    turtle.speed(0)
    turtle.hideturtle()

    turtle.colormode(255)
    turtle.color(
        random.randrange(0, 257, 10),
        random.randrange(0, 257, 10),
        random.randrange(0, 257, 10),
    )
    turtle.begin_fill()
    for i in range(0, 2):
        turtle.forward(280)
        turtle.right(90)
        turtle.forward(280)
        turtle.right(90)
    turtle.end_fill()
    turtle.color(
        random.randrange(0, 257, 10),
        random.randrange(0, 257, 10),
        random.randrange(0, 257, 10),
    )
    turtle.goto(-175, 25)
    turtle.shape("turtle")
    for i in range(5, 60, 2):
        turtle.stamp()
        turtle.forward(30)
        turtle.right(24)
    turtle.goto(0,0)

def drawPostcard(name, adress, postCode, state):
    turtle.penup()
    turtle.hideturtle()

    turtle.color("black")
    nameFont = ("Arial", 20, "normal", "bold")
    textFont = ("Arial", 18, "normal", "bold")

    turtle.write(name, font=nameFont)
    text = [adress, postCode, state]
    for i in range(0, 3):
        turtle.right(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.write(text[i], font=textFont)

    drawPicture()


drawPostcard("Petronela Staňová", "Opatovská cesta 7", "040 01 Košice", "SLOVENSKO")
