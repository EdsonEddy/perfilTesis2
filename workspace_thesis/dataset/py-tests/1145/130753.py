x=int(input())
for j in range(x):
    n=int(input())
    a=0
    b=1
    s=0
    for i in  range(n-1):
        s=a+b
        a=b
        b=s
    print(b)
