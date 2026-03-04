list1 = []

for i in range(1, 31, 1):
    if (10 < i < 21):
        pass
    else:
        k = i * i
        if (k % 2 == 0):
            list1.append(i)

print(list1)
