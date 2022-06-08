while True:
    t=int(input())
    m=list(tuple(map(int,input().split())))
    w=list(set(m))
    d=[]
    p=0
    for i in range(len(w)):
        cont=m.count(w[i])
        d.append(cont)

    for g in range(len(d)):
        p=p+d[g]//2
    print(p)
        