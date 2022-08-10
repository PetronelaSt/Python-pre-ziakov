import turtle


def polygon(numOfSides, sizeOfSides):
    exteriorAngle = 360 / numOfSides
    for i in range(numOfSides):
        turtle.forward(sizeOfSides)
        turtle.right(exteriorAngle)


numOfSides = int(input("Koľko strán bude mať polygón? "))
sizeOfSides = int(input("Aká veľká má byť jedna strana polygónu? "))
polygon(numOfSides, sizeOfSides)



