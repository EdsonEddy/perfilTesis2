ncasos=int(input())
for _ in range(ncasos):
    n = int(input())
    a,b=0,1
    c=0
    if n==0:
        print(c)
        c=c+1
    else:
        for i in range (50):
            c=c+1
            a,b=b,a+b
            if a==n:
                print(c)
                break

