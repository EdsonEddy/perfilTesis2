import sys
for casos in sys.stdin:
    n,k=map(int,casos.split())
    m=(n+1)//2
    if k<=m:
        print(k*2-1)
    else :
        print((k-m)*2)
