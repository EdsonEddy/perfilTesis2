from sys import stdin

for j in stdin:
    p = int(j)
    n = 99
    a, b = -1, 1
    s = 0
    for i in range(n):
        s = a + b
        a, b = b, s
        if p == i:
            print(s)
            break