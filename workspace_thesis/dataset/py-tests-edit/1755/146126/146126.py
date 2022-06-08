while True:
    n=int(input())
    for i in range(n):
        a,b=map(int,input().split())
        r=[1]*b
        d=0
        for j in range(a):
            x=0
            for i in range(0,b,1):
                y=r[d+i]
                x=x+y
            r.append(x)
            d+=1
        print(r[a])
