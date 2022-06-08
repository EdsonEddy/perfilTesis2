y=int(input())
for w in range (y):
    x,a=map(int,input().split())
    b=(("1 ")*a).split()
    d=[]
    for c in b:
        d.append(int(c))
    d.append(a)
    for e in  range(x+1):
        f=0
        f=d[len(d)-a:len(d)]
        h=0
        for g in f:
            h=h+g
        d.append(h)
    print(d[x])