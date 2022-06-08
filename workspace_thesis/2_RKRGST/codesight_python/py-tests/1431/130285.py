n, m, f1, f2 = map(int,input().split())
if n==1:
    r=f1%m
    print(r)
elif n==2:
    r=f2%m
    print(r)
else:
    for i in range(2,n):
        f=f1+f2
        f1=f2
        f2=f
    r=f%m
    print(r)