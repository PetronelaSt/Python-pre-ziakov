def is_prime_number(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                print("Toto nie je prvočíslo")
                break
        else:
            print("Toto je prvočíslo")
    else:
        print("Toto nie je prvočíslo")


n = int(input("Napíš číslo, o ktorom chceš vedieť, či je prvočíslom: "))
is_prime_number(n)

