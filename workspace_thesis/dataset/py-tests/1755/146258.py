veces=int(input())
while veces>0:
    x,y=map(int,input().split())
    v=[1]*y
    s=0
    # g=0
    for i in range(x-1):
        for j in range(i,y):
            s=s+v[j]
        y=y+1
        #for j in range(x):
        #  s=
        v.append(s)
        s=0
    print(v[x])
    veces-=1
