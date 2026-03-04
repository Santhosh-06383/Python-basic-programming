def count(t):
    counts = {"u": 0, "l": 0}
    for c in t:
        if c.isupper():
            counts["u"] += 1
        elif c.islower():
            counts["l"] += 1
    return counts

u = input("Enter a string: ")
result = count(u)

print(f"Uppercase count: {result['u']}")
print(f"Lowercase count: {result['l']}")
