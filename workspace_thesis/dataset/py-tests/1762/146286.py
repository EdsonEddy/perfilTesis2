import sys
for l in sys.stdin:
    z = int(l)
    n = list(tuple(map(int, input().split())))
    c = list(set(n))
    r = []
    a = 0
    for i in range(len(c)):
        cont = n.count(c[i])
        r.append(cont)

    for j in range(len(r)):
        a = a + r[j] // 2
    print(a)