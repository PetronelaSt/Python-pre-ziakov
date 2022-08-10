def remove_duplicates(sentence):
    words = sentence.split()
    sWOD = []
    for word in words:
        if sentence.count(word) > 1 and (word not in sWOD) or sentence.count(word) == 1:
            sWOD.append(word)
    print(" ".join(sWOD))


remove_duplicates(input("Zadaj vetu: "))


