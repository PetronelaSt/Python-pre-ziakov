import random

number = random.randint(0, 100)
print("Máš tri pokusy na uhádnutie čísla!\n")
count = 0

while count < 3:
    count += 1
    guess = int(input("Hádaj číslo: "))

    if number == guess:
        print("Vyhral si! ")
        break
    elif number > guess:
        print("Hádaš príliš malé číslo!")
    elif number < guess:
        print("Hádaš príliš veľké číslo!")

if count >= 3:
    print("Hádané číslo bolo: ", number)

