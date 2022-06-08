while True:
    z=int(input())
    n=list(tuple(map(int,input().split())))
    c=list(set(n))
    r=[]
    x=0
    for i in range(len(c)):
        cont=n.count(c[i])
        r.append(cont)
    
    for j in range(len(r)):
        x=x+r[j]//2
    print(x)