def onlyLetters(s):
    i = 0
    while i < len(s)-1:
        while i==0 and s[i] == " ":
            s = s[i+1:]
        if s[i] == " " and s[i+1] == " ":
            s = s[:i] + s[i+1:]
        else:
            i += 1
    return s

print(onlyLetters("  Ahijbf kdhfn jhd    fij s    "))
