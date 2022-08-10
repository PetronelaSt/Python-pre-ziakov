# D = b^2 – 4*a*c
print("Kvadratická funkcia v tvare : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    num_roots = 2
    x1 = ((-b) + D ** (1 / 2)) / (2 * a)
    x2 = ((-b) - D ** (1 / 2)) / (2 * a)
    print("Rovnica má 2 korene: %f a %f" % (x1, x2))
elif D == 0:
    num_roots = 1
    x = (-b) / (2 * a)
    print("Rovnica má 1 koreň: ", x)
else:
    num_roots = 0
    print("D < 0, rovnica nemá riešenie v množine reálnych čísel.")
