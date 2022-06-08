import sys
for n in sys.stdin:
    n=int(n)
    v=list(map(int,input().split()))
    aux=[]
    c=0
    aux=[v[i] for i in range(len(v))]
    for i in range(n-2):
        if(aux[i+1]<aux[i] and aux[i+1]<aux[i+2]):
            c+=1
    for i in range(n-2):
        if(aux[i+1]>aux[i] and aux[i+1]>aux[i+2]):
            c+=1
    print(c)