def jeIPv4(adresa):
    a = adresa.split(".")
    if len(a) != 4:
        return False
    for i in a:
        if not i.isdigit():
            return False
        j = int(i)
        if j < 0 or j > 256:
            return False
        return True


print(jeIPv4("10000.10.255.3"))
