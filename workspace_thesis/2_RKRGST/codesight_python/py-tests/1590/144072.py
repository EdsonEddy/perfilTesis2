q=0
while q!="":
    n,a,b=map(int,input().split())
    l=[x for x in range(1,n+1)]
    s=0
    for i in l:
        k=str(i)
        u=int(i)
        o=0
        for g in k:
            o=o+int(g)
        if a<=o and o<=b:
            s=s+u
    print(s)