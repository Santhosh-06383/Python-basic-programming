def primefactor(n):
    i = 2
    while n != 1:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i += 1

t = int(input("Enter a number:"))

if t == 1:
    print("1")
else:
    primefactor(t)
