def isAnagram(a, c):
    b = c - a
    aDigits = [int(x) for x in str(a)]
    bDigits = [int(x) for x in str(b)]

    aDigits.sort()
    bDigits.sort()

    if aDigits == bDigits:
        print("Existuje anagram")
    else:
        print("Neexistuje anagram")


isAnagram(int(input("zadaj a: ")), int(input("zadaj c: ")))


