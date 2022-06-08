while True:
    z=int(input())
    n=list(tuple(map(int,input().split())))
    x=list(set(n))
    r=[]
    a=0
    for w in range(len(x)):
        cont=n.count(x[w])
        r.append(cont)    
    for f in range(len(r)):
        a=a+r[f]//2
    print(a)