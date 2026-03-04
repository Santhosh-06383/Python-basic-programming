def sort_dict(n, d):
    a = int(input("Enter the element: "))
    d[n + 1] = a

    print("Before sort:", d)

    sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    print("Sorted (Descending):", sorted_d)

c = {1: 20, 2: 32, 3: 47, 4: 7, 5: 27}

print("Actual Dictionary: ", c)

sorted_a = dict(sorted(c.items(), key=lambda x: x[1]))
print("Sorted (Ascending):", sorted_a)

n = len(c)
sort_dict(n, c)
