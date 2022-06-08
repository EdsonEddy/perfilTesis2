n=int(input())
for i in range (n):
    x=input().split()
    a=-1
    b=0
    for j in x:
        d=int(j)
        if d>b:
            a=a+1
        b=d
    print(a)   