for x in range(500, 526):
    temp = x
    y = x % 10
    if (y != 7 and y % 2 != 0):
        print(temp)
    else:
        continue
