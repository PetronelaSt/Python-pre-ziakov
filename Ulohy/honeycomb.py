import turtle

def hex(size):
    for i in range(6):
        turtle.right(60)
        turtle.forward(size)


def honeycomb(count, size):
        for i in range(0, count):
            hex(size)
            turtle.left(60)
            turtle.forward(size)


honeycomb(int(input("Počet: ")), int(input("Veľkosť: ")))
