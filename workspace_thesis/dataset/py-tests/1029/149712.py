while True:
    v = list(map(int,input().split()))
    aux = 0
    for i in range(len(v)-1):
        for j in range(i,-1,-1):
            if (v[j+1]>v[j]):
                aux = v[j+1]
                v[j+1] = v[j]
                v[j] = aux
    a = 0
    b = 0
    summ = 0
    for i in range(len(v)):
        if (summ == 0):
            a = a+v[i]
            summ = 1
        else:
            b = b+v[i]
            summ = 0
    if (b > a):
        res = b-a
    else:
        res = a-b
    print(res)
