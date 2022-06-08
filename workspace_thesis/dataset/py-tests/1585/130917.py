n=0
while n!=" ":
    n=int(input())
    x=list(range(1,n))
    h=input().split()
    v=input().split()
    s=0
    p=0
    for i in h:
        k=int(i)
        if k in x:
            s=s+1

    for g in v:
        j=int(g)
        if j in x:
            p=p+1
    r=(p+1)*(s+1)
    print(r)