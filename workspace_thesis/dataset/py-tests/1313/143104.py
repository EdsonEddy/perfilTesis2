from sys import stdin
for n in stdin:
    n = int(n)
    v = list(map(int, input().split()))
    v.sort()
    Max = 0
    for i in range(len(v)):
        Max = max(Max, v[i]*(len(v)-i))
    print(Max)
