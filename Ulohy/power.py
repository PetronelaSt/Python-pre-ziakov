def powerOfNumber(a, b):
    if b == 0:
        return 1
    power = a
    increment = a
    for i in range(1, b):
        for j in range(1, a):
            power += increment
        increment = power
    return power


print(powerOfNumber(int(input("Zadaj mocnenca: ")), int(input("Zadaj mocniteľa: "))))
