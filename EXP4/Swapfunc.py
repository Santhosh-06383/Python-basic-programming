def swap(c, d):
    c = c + d
    d = c - d
    c = c - d
    print(f"After swapping: c={c}, d={d}")

s = int(input("Enter a number      : "))
t = int(input("Enter another number: "))

print(f"Before swapping: c={s}, d={t}")
swap(s, t)
