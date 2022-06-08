while True:
    n=int(input())
    s=list(input().split())
    s.sort()
    cr=0
    x=0
    r=[]
    for i in range(0,n,1):
        x=int(s[i])
        if x not in r:
            r.append(x)
            y=s.count(str(x))
            y=y//2
            cr+=y
    print(cr)