def rightNumber():
    text = "3A1B7"
    for a in range(0, 10):
        for b in range(0, 10):
            number = text.replace("A", str(a)).replace("B", str(b))
            if int(number) % 7 == 0 and int(number) % 13 == 0:
                print(number)
                return


rightNumber()
