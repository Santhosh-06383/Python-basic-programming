"""
Experiment 2 - Program 4
Find the sum of digits of a number.
"""

number = int(input("Enter a number: "))
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print(f"Sum of digits is: {total}")
