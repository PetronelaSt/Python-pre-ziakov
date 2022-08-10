def findPattern(pattern, text):
    idxs = ""
    for textIdx in range(len(text) - len(pattern) + 1):
        patternIdx = 0
        while patternIdx < len(pattern):
            if text[textIdx + patternIdx] != pattern[patternIdx]:
                break
            patternIdx += 1
        if patternIdx == len(pattern):
            idxs = idxs + str(textIdx) + ", "
    if len(idxs) != 0:
        print("Vzor bol nájdený na indexoch:", idxs)
    else:
        print("Vzor nebol nájdený.")


text = input("Vložte text: ")
pattern = input("Vložte hľadaný vzor: ")
findPattern(pattern, text)
