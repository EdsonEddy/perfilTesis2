def fibo(x):
    a,b=1,0
    for i in range(x):
        a,b=b,a+b
    return b
n=int(input())
t=y=1
for i in range(n):
    if i%2==0:
        print(fibo(y))
        y+=1
    else:
        print(t*2)
        t+=1