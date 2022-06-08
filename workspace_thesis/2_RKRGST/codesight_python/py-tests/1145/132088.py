t=int(input())
i=1
while i<=t:
    i=i+1
    n=int(input())
    a=1
    b=0
    c=0
    x=(n-1)
    for conteo in range(0, x):
        c=b
        b=a
        a=c+b
    print(a)