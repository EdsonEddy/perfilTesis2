n,m,a,b=map(int,input().split())
c=0
for i in range(n-2):
    c=a+b
    if c>=m:
        c=c%m
        a,b=b,c
    else:
        a,b=b,c
print(c)

