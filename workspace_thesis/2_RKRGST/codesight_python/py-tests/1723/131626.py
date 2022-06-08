from sys import *
for line in stdin:
    a, b = map(int, line.split())
    a, b = str(a), str(b)
    c = 0
    for i in range(len(a)):
        if b[i]!= a[i]:
            c = c +1
    if c > 1:
        print("lentes")
    else:
        print("feliz")
