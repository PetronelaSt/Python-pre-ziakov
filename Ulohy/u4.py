list_of_pn = []


def prime_numbers(x, y):
    for i in range(x, y + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                list_of_pn.append(i)
    print(list_of_pn)


x = 1
y = 100
prime_numbers(x, y)

