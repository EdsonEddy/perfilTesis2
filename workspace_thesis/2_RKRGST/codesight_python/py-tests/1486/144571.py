n=int(input())
def fib(n):
    a=1
    b=1
    for i in range(n):
        a,b=a+b,a
    return(b)

for i in range(n):
    f=fib(i//2)
    if i%2==0:
        print(f)
    else:
        print(2*((i//2)+1))