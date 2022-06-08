import sys
for n in sys.stdin:
    n=int(n)
    v=list(map(int,input().split()))
    aux=[]
    m=0
    may=0
    aux=[v[i] for i in range(len(v))]
    aux.sort()
    for i in range(n):
        if(aux[i]!=0):
            t=aux[i]
            m=0
            for j in range(n-i):
                m=m+t
            if(m>may):
                may=m
    print(may)
    