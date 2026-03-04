def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

num = int(input("Enter a number: "))

if num < 0:
    print("Invalid input")
elif num == 0:
    print("Factorial of 0 is: 1")
else:
    print(f"Factorial of {num} is:", fact(num))
