import sys
for a in sys.stdin:
    a=int(a)
    b=input().split()
    d=0
    e=999999999
    for c in b:
        c=int(c)
        if(e>c):
            e=c
        if(c>d):
            d=c
        else:
            d=d
    print(d-e)
