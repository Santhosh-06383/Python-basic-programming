def emptyfunc(list1, list2):
    print(f"List 1 is {'empty' if not list1 else 'not empty'}")
    print(f"List 2 is {'empty' if not list2 else 'not empty'}")

def commonfunc(list1, list2):
    return not set(list1).isdisjoint(set(list2))

def removefunc(tar, ele):
    while ele in tar:
        tar.remove(ele)
    return tar

m = input("Enter the numbers: ")
l1 = m.split(',')

n = input("Enter the numbers: ")
l2 = n.split(',')

emptyfunc(l1, l2)

common = commonfunc(l1, l2)
print(f"Do the lists have common members? {common}")

val = input("Enter the element to remove: ")

l1 = removefunc(l1, val)
l2 = removefunc(l2, val)

print(f"Lists after removing {val}: L1: {l1}, L2: {l2}")

list3 = []
li1 = []
li2 = []

for x in l1:
    li1.append(int(x))

for y in l2:
    li2.append(int(y))

for a, b in zip(li1, li2):
    if (a + b) > 40:
        list3.append(a + b)

print(f"List 3 (Sums > 40): {list3}")
