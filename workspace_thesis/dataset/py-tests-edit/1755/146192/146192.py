casos=int(input())
for ll in range(casos):
    a,b=map(int,input().split())
    j=0
    fib=[1]*b
    if b>a:
        print(1)
    else:
        for i in range(b,a+1):
            j=sum(fib)
            fib.append(j)
            fib.remove(fib[0])
        print(j)