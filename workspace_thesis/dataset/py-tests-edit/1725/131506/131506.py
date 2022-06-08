from sys import stdin
for i in stdin:
    a,b=map(int,i.split())
    s=0
    i=0

    while b>0:

        c=2**i
        b=b-(c*a)
        s=s+1
        i = i + 1
    print(s)
