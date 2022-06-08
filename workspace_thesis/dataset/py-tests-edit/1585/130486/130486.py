import sys
for a in sys.stdin:
    a=int(a)
    b=input().split()
    d=input().split()
    x=0
    y=0
    for c in b:
        c=int(c)
        if(c<a):
            x=x+1
    for e in d:
        e=int(e)
        if(e<a):
            y=y+1
    print((x+1)*(y+1))
