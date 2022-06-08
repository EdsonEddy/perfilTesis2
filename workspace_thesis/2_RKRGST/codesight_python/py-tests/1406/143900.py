while True:
    g=int(input())
    c,s=0,0
    if g!=0:
        m=list(map(int,input().split()))
        k=list(map(int,input().split()))
        for i in range(g):
            t=m[i]+k[i]
            s=s+t
        p=s/g
        for j in range(g):
            if p>m[j]+k[j]:
                c=c+1
        print(c)
        s,c=0,0