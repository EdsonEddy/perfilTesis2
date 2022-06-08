n=int(input())
a=-1
b=1
while n>=0:
    a = -1
    b = 1
    for i in range(n+1):
        c=a+b
        a=b
        b=c
    print(c)
    n=int(input())