s = input("enter the string:")

if len(s) >= 3:
    if s.endswith('ing'):
        s += 'ly'
    else:
        s += 'ing'
    print(s)
else:
    print("The string is less than 3, string is: ", s)
