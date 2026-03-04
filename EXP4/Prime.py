def prime(n):
    flag = 0
    for y in range(2, n):
        if n % y == 0:
            flag = 1
    if flag == 1:
        return 0
    else:
        return 1

num = int(input("Enter a number:"))
print(prime(num))
