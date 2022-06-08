while 2>0:
    veces=int(input())
    puntos=input()
    c=0
    c2=0
    m=puntos.split(" ")
    may=0
    for e in m:
        if c==veces:
            break
        c = c + 1
        e1=int(e)
        if e1 > may:
            may=e1
    min=may
    for e in m:
        if c2==veces:
            break
        c2 = c2 + 1
        e2=int(e)
        if e2 < min:
            min=e2
    dis=may-min
    print(dis)