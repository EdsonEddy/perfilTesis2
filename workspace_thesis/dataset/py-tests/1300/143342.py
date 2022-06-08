from sys import stdin
for j in stdin:
    n = int(j)
    m = [int(x) for x in input().split()]
    cn = 0
    for i in range(n):
        if m[i] == m[n - 1]:
            cn += 1
    print(cn)