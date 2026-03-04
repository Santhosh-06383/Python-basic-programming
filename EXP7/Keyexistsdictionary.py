def mergedicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

def checkkey(d, key):
    if key in d:
        print("Key exists in the merged dictionary.")
    else:
        print("Key does NOT exist in the merged dictionary.")

n1 = int(input("Enter number of elements in first dictionary: "))
dict1 = {}

for i in range(n1):
    k = int(input("Enter key: "))
    v = int(input("Enter value: "))
    dict1[k] = v

n2 = int(input("\nEnter number of elements in second dictionary: "))
dict2 = {}

for i in range(n2):
    k = int(input("Enter key: "))
    v = int(input("Enter value: "))
    dict2[k] = v

newdict = mergedicts(dict1, dict2)

print("\nMerged dictionary:", newdict)

searchkey = int(input("\nEnter key to search: "))
checkkey(newdict, searchkey)
