while True:
    x=int(input())
    n=list(tuple(map(int,input().split())))
    c=list(set(n))
    r=[]
    s=0
    for i in range(len(c)):
        cont=n.count(c[i])
        r.append(cont)
    
    for j in range(len(r)):
        s=s+r[j]//2
    print(s)