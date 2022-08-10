def countCurrency(amount):

    notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]

    noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    print("Currency Count -> ")

    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print(i, " : ", j)


def countCurrency2(amount):
    notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Počet potrebných bankoviek a mincí na vyplatenie sumy " + str(amount) + ":")
    for i in range(0, len(notes)):
        if amount >= notes[i]:
            noteCounter[i] = amount // notes[i]
            amount = amount - noteCounter[i] * notes[i]
            print(notes[i], "€ : ", noteCounter[i])


amount = int(input("Zadaj sumu: "))
countCurrency2(amount)
