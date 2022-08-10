def lifePathNumber(dateOfBirth):
    lpn = 0
    for digit in dateOfBirth:
        lpn += int(digit)
        if lpn > 9:
            lpn = lpn % 10 + lpn // 10
    return str(lpn)


dateOfBirth = input("Zadajte dátum vášho narodenia v tvare DDMMRRRR: ")
print("Vaše životné číslo je: " + lifePathNumber(dateOfBirth))

