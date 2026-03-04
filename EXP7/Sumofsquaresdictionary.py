def sum_of_squares(a, n):
    total = 0
    for i in range(1, n + 1):
        total += a[i]
    return total

n = int(input("Enter number: "))
a = dict()

for j in range(1, n + 1):
    a[j] = j * j

print("Dictionary:", a)
print("The sum of squares:", sum_of_squares(a, n))
