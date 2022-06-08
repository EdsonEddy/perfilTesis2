from sys import stdin

for x in stdin:
    n = int(x)
    a = list(map(int, input().split()))
    m = int(input())
    a.sort()
    for i in range(n):
        b = m - a[i]
        if b in a:
            for j in range(n):
                if b == a[j]:
                    s = a[j]
            print(a[i], s)
            break
    else:
        print('-1')