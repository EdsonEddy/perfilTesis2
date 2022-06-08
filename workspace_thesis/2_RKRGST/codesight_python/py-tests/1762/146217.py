while True:
    a = int(input())
    b = list(tuple(map(int, input().split())))
    c = list(set(b))
    r = []
    e = 0
    for i in range(len(c)):
        cont = b.count(c[i])
        r.append(cont)

    for n in range(len(r)):
        e = e + r[n] // 2
    print(e)