def max(m, n, p):
    if (m > n and m > p):
        a = m
    elif (n > p):
        a = n
    else:
        a = p
    return a

s = int(input("Enter first number : "))
t = int(input("Enter second number: "))
u = int(input("Enter third number : "))

print("The greatest number is: ", max(s, t, u))
