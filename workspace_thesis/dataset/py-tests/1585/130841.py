from sys import stdin

for j in stdin:
    n = int(j)
    h = [int(a) for a in input().split()]
    v = [int(b) for b in input().split()]
    ch, cv = 0, 0
    for i in range(3):
        if h[i] < n:
            ch = ch + 1
        if v[i] < n:
            cv = cv + 1
    nc = (cv + ch) + (cv * ch) + 1
    print(nc)