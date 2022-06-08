def fibo(x):
    a=1
    b=0
    for i in range(1,x+1):
        c=a+b
        a=b
        b=c
        
    return c
def par(x):
    return x*2

while True:
    n=int(input())
    x=1
    y=1
    for i in range(1,n+1):
        if i%2==0:
           print( par(x))
           x=x+1
        else:
            print(fibo(y))
            y=y+1
