n,m=map(int,input().split())
c=1
col=10
while col<=n:
    c=c+1
    col=col*10
c1=1
n1=str(n)
cinv=n1[::-1]
cinv=int(cinv)
while c1<=m:
    f=cinv%10
    g=cinv//10
    c1=c1+1
    cinv=g
print(c,f)