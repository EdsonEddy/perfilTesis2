def pares(x):
    return 2*x
def fibo(x):
    a,b=1,0
    for i in range(x):
        a,b=b,a+b
    return(b)
c,d=1,1
for i in range(int(input())):
    if i%2==1:
        print(pares(c))
        c=c+1
    else:
        print(fibo(d))
        d=d+1