import sys
for n in sys.stdin:
    n=int(n)
    b=0
    aux=0
    cad=input()
    v = cad.split(" ")
    for i in range(n):
        v[i]=int(v[i])
    v.sort()
    for j in range(n):
        a=v[j]*(n-b)
        b=b+1
        if (a>aux):
            aux=a
    print(aux)