import sys
for j in sys.stdin:
    n=int(j)
    if(n<100):
        a = 0
        b = 1
        for i in range(1,n+1):
            a,b=b,a+b
        print(a)
    else:
        exit()