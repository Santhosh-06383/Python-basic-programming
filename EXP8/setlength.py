n = int(input("Enter the size:"))
s = set()

for i in range(n):
    e = int(input("Enter the elements: "))
    s.add(e)

print("set is: ", set(s))
print("length of set:", len(s))

def search(i):
    x = int(input("element to be searched:"))
    if x in i:
        print("The element ", x, " exists in the set")
    else:
        print("The element ", x, " is not present in the list")

search(s)
