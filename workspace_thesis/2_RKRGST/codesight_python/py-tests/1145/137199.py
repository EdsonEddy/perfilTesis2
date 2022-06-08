n=int(input())
for i in range(1,n+1):
    x=int(input())
    a=1
    b=0
    for j in range(1,x+1):
        f=a+b
        a=b
        b=f
    print(f)