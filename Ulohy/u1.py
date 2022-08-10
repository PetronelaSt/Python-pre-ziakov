import random


def n_max_numbers(random_list, n):
    final_list = []
    for i in range(0, n):
        max_number = 0
        for j in range(len(random_list)):
            if random_list[j] > max_number:
                max_number = random_list[j]
        random_list.remove(max_number)
        final_list.append(max_number)
    print(final_list)


x = 5
y = 100
k = 10

random_list = list(random.randint(x, y) for i in range(k))
print(random_list)

n = 3
n_max_numbers(random_list, n)
