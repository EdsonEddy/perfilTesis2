from sys import stdin
for line in stdin:
    c = list(map(int, line.split()))
    c.sort()
    uno = sum(c[::2])
    dos = sum(c[1::2])
    print(abs(uno-dos))