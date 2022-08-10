string = input("Napíš ľubovolné slovo: ")
length = len(string) + 1
for i in range(1, length):
    for j in range(0, length):
        print(end=".")
    length = length - 1
    for j in range(length, 0, -1):
        print(string[j], end="")
    print(" ")
