s1 = input("enter the string:")

d = 0
s = 0
a = 0

for c in s1:
    if c.isdigit():
        d += 1
    elif c.isspace():
        s += 1
    elif c.isalpha():
        a += 1

print("Digits    : ", d)
print("Spaces    : ", s)
print("Alphabets : ", a)
