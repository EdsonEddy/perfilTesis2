n=int(input())
for i in range(n):
    x=input().split()
    c=-1
    ma=0
    for j in x:
        d=int(j)
        if d>ma:
            c=c+1
        ma=d
    print(c)