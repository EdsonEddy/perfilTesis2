while True:
    j=int(input())
    p=list(tuple(map(int,input().split())))
    h=list(set(p))
    r=[]
    v=0
    for i in range(len(h)):
        cont=p.count(h[i])
        r.append(cont)
    
    for j in range(len(r)):
        v=v+r[j]//2
    print(v)