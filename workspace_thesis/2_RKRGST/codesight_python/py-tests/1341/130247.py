import sys
for i in sys.stdin:
    n=int(i)
    a=-1
    b=1
    for i in range(n+1):
        s=a+b
        a=b
        b=s
    print(s)