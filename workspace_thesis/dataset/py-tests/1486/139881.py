x=int(input())
c=0
a=1
b=0
for i in range(1,x+1):
    if i%2==0:
        c=c+2
        print(c)
    else:
        fibo=a+b
        a=b
        b=fibo
        print(fibo)
        