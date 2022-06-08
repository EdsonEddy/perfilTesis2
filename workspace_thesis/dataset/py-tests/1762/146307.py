while True:
    y=int(input())
    m=list(tuple(map(int,input().split())))
    d=list(set(m))
    p=[]
    s=0
    for i in range(len(d)):
        cont=m.count(d[i])
        p.append(cont)
    
    for j in range(len(p)):
        s=s+p[j]//2
    print(s)