import turtle  # Allows us to use turtles

turtle.setup(400, 600)  # Determine the window size
tess = turtle.Turtle()  # Create a turtle, assign to tess
alex = turtle.Turtle()  # Create alex
henry = turtle.Turtle()  # Create henry

def draw_housing():
    tess.pensize(3)  # Change tess' pen width
    tess.color('black', 'white')  # Set tess' color
    tess.begin_fill()  # Tell tess to start filling the color
    tess.forward(80)  # Tell tess to move forward by 80 units
    tess.left(90)  # Tell tess to turn left by 90 degrees
    tess.forward(250)
    tess.left(90)
    tess.forward(80)  # Tell tess to move forward by 80 units
    tess.left(90)  # Tell tess to turn left by 90 degrees
    tess.forward(250)
    tess.left(90)
    tess.end_fill()  # Tell tess to stop filling the color


draw_housing()


def circle(t, ht, colr):
    """Position turtle onto the place where the lights should be, and
    turn turtle into a big circle"""
    t.penup()  # This allows us to move a turtle without drawing a line
    t.forward(40)
    t.left(90)
    t.forward(ht)
    t.shape('circle')  # Set tutle's shape to circle
    t.shapesize(3)  # Set size of circle
    t.fillcolor(colr)  # Fill color in circle


circle(tess, 50, 'green')
circle(alex, 120, 'orange')
circle(henry, 190, 'red')
