import sys
for linea in sys.stdin:
    n=int(linea)
    a,b=-1,1
    for i in range(n+1):
        f=a+b
        a=b
        b=f
    print(f)