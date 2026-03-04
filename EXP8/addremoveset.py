x = int(input("enter the range:"))
list1 = []

for i in range(x):
    n = int(input("enter list elements:"))
    list1.append(n)

print("list:", list1)

s = set(list1)
print("set:", s)

def adding(i):
    z = int(input("enter element to add:"))
    i.add(z)
    print("added set:", i)

def removing(j):
    y = int(input("enter element to remove:"))
    j.remove(y)
    print("removed set:", j)

adding(s)
removing(s)
