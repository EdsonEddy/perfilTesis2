e=int(input())
for a in range(1,e+1):
    a=int(input())
    b=1
    c=0
    x=0
    for d in range(1,a+1):
        x=x+1
        x=b+c
        b=c
        c=x
    print(x)