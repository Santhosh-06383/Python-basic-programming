"""
Experiment 1 - Program 3
Swap two numbers.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

num1, num2 = num2, num1

print(f"After swapping: num1 = {num1}, num2 = {num2}")
