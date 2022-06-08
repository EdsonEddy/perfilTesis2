z=int(input())
for q in range(z):
    r,c=map(int,input().split())
    s=0
    p=0
    for i in range(r):
        c=""
        v=input().split()
        for u in v:
            c=c+u
        if s%2==0:
            for k in range(0,len(c),2):
                b=int(c[k])
                p=p+b
        else:
            for m in range(1,len(c),2):
                b=int(c[m])
                p=p+b
        s=s+1
    print(p)