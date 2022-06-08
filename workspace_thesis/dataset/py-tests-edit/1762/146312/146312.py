while True:
    t = int(input())
    k = list(tuple(map(int, input().split())))
    w = list(set(k))
    g = []
    s = 0
    for i in range(len(w)):
        cont = k.count(w[i])
        g.append(cont)

    for j in range(len(g)):
        s = s + g[j] // 2
    print(s)