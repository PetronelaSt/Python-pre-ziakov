def fibonacci(n):
    fibonacci = [0, 1, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[n]


n = int(input("Napíš poradie fibonacciho čísla, ktoré chceš poznať: "))
print(fibonacci(n))

