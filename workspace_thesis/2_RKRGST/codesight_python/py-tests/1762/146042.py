from sys import stdin

for x in stdin:
    m = int(x)
    n = list(map(int, input().split()))
    n.sort()
    cp = 0
    i = 0
    while i < len(n) - 1:
        if n[i] == n[i + 1]:
            cp = cp + 1
            i = i + 2
        else:
            i = i + 1
    print(cp)
