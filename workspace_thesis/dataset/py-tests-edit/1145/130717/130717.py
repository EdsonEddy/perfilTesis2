def fibo(x):
    a=-1
    b=1
    for i in range(x+1):
        c=a+b
        a=b
        b=c
    return(c)
n=int(input())
for i in range(n):
    x=int(input())
    if 1<=x<=200:
        c=fibo(x)
        print(c)