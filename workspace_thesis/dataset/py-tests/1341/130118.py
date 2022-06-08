import sys
for l in sys.stdin:
    a,b,c=1,0,0
    n=int(l)
    if n<100:
         for i in range(n):
             c=a+b
             a=b
             b=c
         print(c)
    else:
        break