num = int(input("Enter the number: "))
fact = 1

if num < 0:
    print("Invalid input (should be >0)")
elif num == 0:
    print("The Factorial of 0 is: 1")
else:
    for i in range(1, num + 1):
        fact *= i
    print(f"The factorial of {num} is: ", fact)
