while True:
    a=int(input())
    n=list(tuple(map(int,input().split())))
    c=list(set(n))
    r=[]
    b=0
    for i in range(len(c)):
        cont=n.count(c[i])
        r.append(cont)
    
    for j in range(len(r)):
        b=b+r[j]//2
    print(b)