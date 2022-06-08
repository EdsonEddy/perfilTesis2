import sys
for a in sys.stdin:
    a=a.split()
    l=len(a)
    c=0
    for i in range(l):
        b=a[i]
        b=int(b)
        c=c+b
    print(c)
    a,b,c=0,0,0