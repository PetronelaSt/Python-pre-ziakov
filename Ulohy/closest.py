import random


def average(numbers):
    return sum(numbers) / len(numbers)


def closest():
    avNum = average(rNumbers)
    print("Priemer čísel je: " + str(avNum))
    idx = []
    for n in rNumbers:
        idx.append(abs(avNum - n))
    print(
        "Číslo najmenej odlišné od priemeru je: " + str(rNumbers[idx.index(min(idx))])
    )


def closest2():
    rNumbers = [random.randrange(1, 101, 1) for i in range(100)]
    print("Vygenerované čísla sú: " + str(rNumbers))
    avNum = average(rNumbers)
    print("Priemer čísel je: " + str(avNum))
    min = 101
    idx = -1
    sortedN = sorted(rNumbers)
    # print("SORTED: " + str(sortedN))
    for n in range(0, len(sortedN), 1):
        if min > abs(avNum - sortedN[n]) and abs(avNum - sortedN[n]) >= 0:
            min = abs(avNum - sortedN[n])
            idx = n
    print("Číslo najmenej odlišné od priemeru je: " + str(sortedN[idx]))



closest2()
