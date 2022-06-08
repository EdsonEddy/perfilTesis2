from sys import stdin
for n in stdin:
    n = int(n)
    v = list(map(int, input().split()))
    maximo = 0
    v.sort()
    for i in range(n):
        d = n-i
        f = v[i] * (d)
        maximo = max(maximo, f)
    print(maximo)