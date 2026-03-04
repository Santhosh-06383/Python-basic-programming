a = int(input("enter the limit: "))

for x in range(1, a + 1):
    print(" " * (a - x), "* " * x)

for y in range(a - 1, 0, -1):
    print(" " * (a - y), "* " * y)
