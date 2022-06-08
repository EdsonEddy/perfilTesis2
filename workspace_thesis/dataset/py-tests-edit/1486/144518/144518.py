def fibo(n):
    a=0
    b=1
    r=[]
    c=0
    while c<n:
        a,b=b,a+b
        r.append(a)
        c+=1
    return r

def par(n):
    d=2
    c=0
    re=[]
    while c<n:
        re.append(d)
        d+=2
        c+=1
    return re

r=int(input())
n=r//2+1
a,b=fibo(n),par(n)
res=[]
for i in range(0,n,1):
    res.append(a[i])
    res.append(b[i])
for j in range(0,r,1):
    print(res[j])
