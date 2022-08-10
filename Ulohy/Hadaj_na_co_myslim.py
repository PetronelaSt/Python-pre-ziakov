# Hadaj na čo myslim

meno = input("Ako sa voláš? ")
# print("Ahoj " + meno) zreťazenie
print("Ahoj", meno)

hadane_slovo = "iterator"

pocet_pokusov = 3

# Pokiaľ pocet_pokusov > 0 : vykonaj
while pocet_pokusov > 0:
    slovo = input("Hádaj ")
    pocet_pokusov = pocet_pokusov - 1

    # Ak nastane podmienka : vykonaj niečo
    # Ak slovo = hadane_slovo : vypiš, že si vyhral
    if slovo == hadane_slovo:
        pocet_pokusov = -1
        print("Vyhral si!")
        # Inak: vykonaj niečo
    if slovo != hadane_slovo and pocet_pokusov == 0:
        print("Prehral si!")
