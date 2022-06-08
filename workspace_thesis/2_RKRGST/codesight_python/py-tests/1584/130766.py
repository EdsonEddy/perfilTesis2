from sys import stdin
for j in stdin:
    n = int(j)
    p = [int(x) for x in input().split()]
    mx = 0
    mn = 1000
    for i in range(n):
        if p[i] > mx:
            mx = p[i]
        if p[i] < mn:
            mn = p[i]
    print(mx-mn)