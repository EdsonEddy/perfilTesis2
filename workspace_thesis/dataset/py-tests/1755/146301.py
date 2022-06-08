casos=int(input())
while casos>0:
    a,b=map(int,input().split())
    m=[1]*b
    s=0
    for i in range(a-1):
        for j in range(i,b):
            s=s+m[j]
        b=b+1
        m.append(s)
        s=0
    print(m[a])
    casos-=1

