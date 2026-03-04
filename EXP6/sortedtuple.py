i = input("Enter the names: ")
tuple1 = tuple(i.split(','))

n = sorted(tuple1)

print("Sorted tuple: ", tuple(n))
