n=int(input())
if 1<n<=5000:
    p,q,r,s,t=map(int,input().split())
    x=p+q+r
    y=s+t
    salida=y-x
    print(salida)
