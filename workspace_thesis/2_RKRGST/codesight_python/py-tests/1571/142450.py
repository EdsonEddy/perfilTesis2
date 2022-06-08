import sys
for n in sys.stdin:
    n=int(n)
    v=list(map(int, input().split()))
    aux=[]
    c=0
    for i in range (1,n-1):
        if ((v[i]<v[i-1] and v[i]<v[i+1]) or (v[i]>v[i-1] and v[i]>v[i+1])):
            c=c+1
    print (c)