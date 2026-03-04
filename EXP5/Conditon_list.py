s = input("Enter the binary inputs:")
list1 = s.split(',')
mylist = []

print(list1)

for x in list1:
    if int(x, 2) % 5 == 0:
        mylist.append(x)

print("Divsible by 5: ", mylist)
