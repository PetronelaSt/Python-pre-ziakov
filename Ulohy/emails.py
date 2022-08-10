def main():
    result = int(input("Číslo na prevod: "))
    # print(hex(result))
    hexadecimal = ""
    while result != 0:
        remainder = changeDigit(result % 16)
        hexadecimal = str(remainder) + hexadecimal
        result = int(result / 16)
    print(hexadecimal)


def changeDigit(digit):
    decimal = [10, 11, 12, 13, 14, 15]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for counter in range(7):
        if digit == decimal[counter - 1]:
            digit = hexadecimal[counter - 1]
    return digit


main()
