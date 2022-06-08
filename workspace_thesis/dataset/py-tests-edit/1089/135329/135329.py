import math

n = int(input(""))
x = 0

a = int(math.log10(n)+1)
b = a / 2

if a % 2 == 0:
    print("*")
else:
    while x <= b:
        d = int(n % 10)
        n = n / 10
        x = x + 1
    print(d)
