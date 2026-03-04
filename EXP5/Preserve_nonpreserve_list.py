t = input("Enter the numbers: ")
list1 = t.split(',')

list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)

print("By preserving the order: ", list2)

list3 = list(set(list1))
print("Order un-preserved: ", list3)
