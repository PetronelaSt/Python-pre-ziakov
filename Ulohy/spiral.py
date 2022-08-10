import turtle

radius = int(input("Zadajte polomer: "))
space = 50
for i in range(100):
    turtle.circle(radius + i, space)

