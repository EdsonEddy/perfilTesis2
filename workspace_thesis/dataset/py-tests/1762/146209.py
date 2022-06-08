while True:
    q = int(input())
    n = list(tuple(map(int, input().split())))
    x = list(set(n))
    r = []
    f = 0
    for i in range(len(x)):
        cont = n.count(x[i])
        r.append(cont)

    for k in range(len(r)):
        f = f + r[k] // 2
    print(f)