sumW = 0
i = 1
while True:
    weight = int(input("Váha " + str(i) + ": "))
    sumW += weight
    if sumW > 500:
        print(
            "Výťah je preťažený! Nosnosť výťahu bola prekročená o "
            + str(sumW - 500)
            + "kg"
        )
        break
    if i >= 6:
        print("Výťah je plný! Max. kapacita výťahu je 6 ľudí!")
        break
    i += 1
