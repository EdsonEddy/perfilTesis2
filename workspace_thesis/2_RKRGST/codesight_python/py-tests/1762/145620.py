import sys
for n in sys.stdin:
    l=list(map(int,input().split()))
    pares=[0]*101
    for i in l:
        pares[i]+=1
    s=0;
    for i in pares:
        s=s+i//2
    print(s)