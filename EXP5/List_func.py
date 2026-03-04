m = input("Enter the number: ")
n = input("Enter the colors: ")

list1 = m.split(',')
list2 = n.split(',')

size = len(list2)

print("Number of colors you have entered is: ", size)
print("Greatest value in list 1: ", max(list1))
print("Smallest value in list 1: ", min(list1))

list3 = []
total = 0

for i in list1:
    list3.append(int(i))

for x in list3:
    total += x

print("Total sum of elements in list 2 is: ", total)
