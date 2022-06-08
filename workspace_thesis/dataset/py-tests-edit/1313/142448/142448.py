import sys
for n in sys.stdin:
    n=int(n)
    v=list(map(int, input().split()))
    v.sort()
    aux=[]
    for i in range (n):
        m=v[i]*(n-i)
        aux.append(m)
    print (max(aux))