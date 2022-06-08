import sys
for a in sys.stdin:
    b,c=map(int,a.split())
    d=input().split()
    e=0
    g=0
    for f in d:
        f=int(f)
        b=b-1
        g=g+f*c**b
    print(float(g))