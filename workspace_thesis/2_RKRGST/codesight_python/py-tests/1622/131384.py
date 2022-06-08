def fib (a,b):
    while True:
        yield a
        a,b = b, a+b
c=int(input())
for i in range(c):
    n=int(input())
    a,b=map(int,input().split())
    f=fib(a,b)
    print("+".join(str(next(f)) for _ in range(n)))