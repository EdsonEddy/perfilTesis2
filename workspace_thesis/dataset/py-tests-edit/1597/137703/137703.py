n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    r1=0
    r2=0
    while a>0:
        r1=r1+a%10
        a=a//10
    while b>0:
        r2=r2+b%10
        b=b//10
    print(max(r1,r2))
