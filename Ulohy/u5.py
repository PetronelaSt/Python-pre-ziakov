def tabOfPower(numOfLines):
    power = 1
    line = 1
    order = 1
    while line <= numOfLines:
        print("\n Mocniny čísla ", line)
        while order <= 10:
            print(power)
            power = power * line
            order += 1
        line += 1
        order = 1
        power = 1


tabOfPower(5)

