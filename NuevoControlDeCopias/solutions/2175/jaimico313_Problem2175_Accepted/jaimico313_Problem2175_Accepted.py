n=int(input())
for i in range(n):
    numero=int(input())
    s=0;a=-1;b=1
    fibo=a+b
    while (fibo!=numero):
        a=b;b=fibo
        fibo=a+b
        s=s+1
    print(s)
