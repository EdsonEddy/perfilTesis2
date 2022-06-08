from sys import stdin
for n in stdin:
    n = int(n)
    v = list(map(int, input().split()))
    Max = 0
    v.sort()
    for i in range(n):
        Max = max(Max, v[i] * (n-i))
    print(Max)