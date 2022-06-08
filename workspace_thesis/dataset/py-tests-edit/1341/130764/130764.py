while True:
    n=int(input())
    a,b=0,1
    for i in range(0,n-1):
        a,b=b,a+b
    if n!=0:
        print(b)
    else:
        print(0)