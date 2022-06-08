from sys import *
for line in stdin:
    a, b = map(int, line.split())
    c = 1
    x = a
    while a!= b:
        c = c + 1
        a = a*2 + x
    print(c)