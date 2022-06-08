import math

z = int(input(""))
r = 0

a = int(math.log10(z)+1)
b = a / 2

if a % 2 == 1:
    while r <= b:
        d = int(z % 10)
        z = z / 10
        r = r + 1
    print(d)
else:
    print("*")
