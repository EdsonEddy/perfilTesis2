n=int(input())
for i in range(n):
    fib=(int(input()))
    a=-1
    b=1
    j=0
    while True:
        c=a+b
        a=b
        b=c
        if c==fib:
            print(j)
            break
        j+=1
