from sys import stdin

for x in stdin:
    n = int(x)
    cn = 0
    while n > 0:
        n = n // 2
        cn = cn + 1
    print(cn)