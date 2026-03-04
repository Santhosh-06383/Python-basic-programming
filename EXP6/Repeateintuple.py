t = input("Enter the tuple: ")
tup2 = tuple(t.split(','))

a = set()
b = set()

for i in tup2:
    if i in b:
        a.add(i)
    else:
        b.add(i)

print("Provided: ", tup2)
print("Repeated: ", tuple(a))
