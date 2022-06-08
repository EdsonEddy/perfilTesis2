n=int(input())
for i in range(n):
    x=int(input())
    a=1
    b=0
    s=0
    for j in range(x):
        s=a+b
        a=b
        b=s
    print(s)
