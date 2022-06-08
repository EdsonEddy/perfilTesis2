N,M,a,b=map(int, input().split())
i=1
while (i <= N):
    c=b-a
    d=b-c
    a=b
    b=b+d
    i=i+1
d=d%M
print (d)