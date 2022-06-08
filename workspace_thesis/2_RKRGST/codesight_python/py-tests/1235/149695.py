n=int(input())
if 1<n<=5000:
    q,w,e,r,t=map(int,input().split())
    x=q+w+e
    y=r+t
    salida=y-x
    print(salida)
