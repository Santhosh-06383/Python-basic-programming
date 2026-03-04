m = input("Enter the number: ")
u = m.split(',')

t = []
for x in u:
    t.append(int(x))

s = []

a = int(input("enter the index1:"))
b = int(input("enter the index2:"))

print("The value is: ", t[a:b])

for i in t[:]:
    if (i % 2 != 0):
        t.remove(i)
        s.append(i)

t.extend(s)

print("Updated list: ", t)
