slovo = "tanap"
slovo = slovo.upper()
print(slovo)

slovo = slovo.lower()
print(slovo)

veta = "Dnes je slnecno."
print(veta.lower())
print(veta.upper())

# replace(co nahradzujem, zaco nahradzujem)
veta = veta.replace("slnecno", "dazdivo")
print(veta)

#veta = veta.replace("d", "c")
#print(veta)

retazec1="Ahoj"
retazec2="ahOj"

if retazec1.lower() == retazec2.lower():
    print("je to rovnake")
else:
    print("lisi sa")

print(retazec1.lower() == retazec2.lower())
print(3<4)

print(veta.find("e"))
print(veta.find("e", 3, 7))

veta = veta.lower()
print(veta)

idx = veta.find("d")
veta = veta[idx].upper() + veta[idx+1:]
print(veta)

basen = "Zletely orli z Tatri, tyahnu na podolya, ponad visoké hori, ponad rovné polya; preletely cez Dunaj, cez tú šýru vodu, sadly tam za pomedzým slovenského rodu."

tvrde = "yý"
makke = "ií"
for i in range(0, len(tvrde)):
    basen = basen.replace(tvrde[i], "*")
    basen = basen.replace(makke[i], tvrde[i])
    basen = basen.replace("*", makke[i])

print(basen)


