n=int(input())
for i in range(n):
    x=input().split()
    a=-1
    ma=0
    for j in x:
        b=int(j)
        if b>ma:
            a=a+1
        ma=b
    print(a)
