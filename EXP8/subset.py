x = int(input("enter range 1:"))
a = set()

for i in range(x):
    e = int(input("enter elements:"))
    a.add(e)

y = int(input("enter range 2:"))
b = set()

for i in range(y):
    e = int(input("enter element:"))
    b.add(e)

print("set a:", a)
print("set b:", b)

if a.issubset(b) == True:
    print("a is subset of b")
elif b.issubset(a) == True:
    print("b is subset of a")
else:
    print("Both are not a sub set")
