items = []
key = "stop"

print("Enter elements and type --- stop --- to finish")

while True:
    a = input("Enter element: ")
    if a.lower() == key:
        break
    items.append(a)

tuple1 = tuple(items)

print("Final Tuple: ", tuple1)
