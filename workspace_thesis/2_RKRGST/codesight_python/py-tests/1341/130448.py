import sys
for n in sys.stdin:
    n=int(n)
    a=1
    b=0
    for i in range(n):
         a,b=b,a+b
    print(b)