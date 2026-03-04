f = input("Enter the elements: ")
tup1 = tuple(f.split(','))

a = int(input("Enter a number: "))

tup2 = set()

for x in range(0, a, 1):
    tup2.add(tup1[x])

print(tuple(tup2))
