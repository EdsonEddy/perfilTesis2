while True:
    x=int(input())
    n=list(tuple(map(int,input().split())))
    d=list(set(n))
    r=[]
    b=0
    for i in range(len(d)):
        cont=n.count(d[i])
        r.append(cont)
    
    for j in range(len(r)):
        b=b+r[j]//2
    print(b)