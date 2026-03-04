x = int(input("enter range for set 1:"))
a = set()
b = set()

for i in range(x):
    e = int(input("enter element:"))
    a.add(e)

y = int(input("enter range for set 2:"))
for i in range(y):
    e = int(input("enter elements:"))
    b.add(e)

print("set a:", a)
print("set b:", b)

print("The union:", a.union(b))
print("The intersection:", a.intersection(b))
print("The difference a to b:", a.difference(b))
print("The difference b to a:", b.difference(a))
