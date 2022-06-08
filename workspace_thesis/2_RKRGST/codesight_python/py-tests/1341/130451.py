n=int(input())
while n>=0:
    a = -1
    b = 1
    s = 0
    for i in range(n+1):
        s=(a+b)
        a=b
        b=s
    print(s)
    n=int(input())
