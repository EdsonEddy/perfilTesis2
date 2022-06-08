while True:
    R = int(input())
    O = list(tuple(map(int, input().split())))
    B = list(set(O))
    E = []
    T = 0
    for i in range(len(B)):
        contador = O.count(B[i])
        E.append(contador)

    for j in range(len(E)):
        T = T + E[j] // 2
    print(T)