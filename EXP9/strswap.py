a = input("Enter string 1:")
b = input("Enter string 2:")

c = b[:2] + a[2:]
d = a[:2] + b[2:]

print("The input string is: ", a, b)
print("The value changed string is: ", c, d)
