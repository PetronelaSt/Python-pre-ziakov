def isPalindrome(string):

    for i in range(0, int(len(string) / 2)):
        if string[i] != string[len(string) - i - 1]:
            print("Nie je palindróm")
            return
    print("Je palindróm")


word = input("Zadaj slovo: ")
isPalindrome(word)

