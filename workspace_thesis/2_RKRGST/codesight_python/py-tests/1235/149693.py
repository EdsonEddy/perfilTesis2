n=int(input())
if 1<n<=5000:
    a,b,c,d,e=map(int,input().split())
    x=a+b+c
    y=d+e
    z=y-x
    print(z)