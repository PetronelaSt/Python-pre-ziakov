print("Kalkulačka")

while True:
    num1 = float(input("Vložte prvé číslo: "))
    choice = input("Zadajte operáciu: ")
    num2 = float(input("Enter second number: "))

    if choice == "+":
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == "-":
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == "*":
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == "/":
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Nepodporovaná operácia")

