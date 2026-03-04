def cfreq(i):
    f = {}
    for c in i:
        if c in f:
            f[c] += 1
        else:
            f[c] = 1
    return f

s = input("Enter the string: ")
result = cfreq(s)

print(result)
