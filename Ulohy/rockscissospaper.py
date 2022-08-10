import random

userAction = input("Vyber si (kamen, papier, noznice): ")
possibleActions = ["kamen", "papier", "noznice"]
computerAction = random.choice(possibleActions)
print("Vybral si si: " + userAction + ", počítač si vybral: " + computerAction + "\n")

if userAction == computerAction:
    print("Obaja hráči zvolili: " + userAction + "\n Je to remíza!")
elif userAction == "kamen":
    if computerAction == "noznice":
        print("Kameň poráža nožnice! Vyhral si! =)")
    else:
        print("Papier zabalí kameň! Prehral si. =(")
elif userAction == "papier":
    if computerAction == "kamen":
        print("Paper zabalí kameň! Vyhral si! =)")
    else:
        print("Nožnice prestrihnú papier! Prehral si. =(")
elif userAction == "noznice":
    if computerAction == "papier":
        print("Nožnice prestrihnú papier! Vyhral si! =)")
    else:
        print("Kameň otupí nožnice! Prehral si. =(")
