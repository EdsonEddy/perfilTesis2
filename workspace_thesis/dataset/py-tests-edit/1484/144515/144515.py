def primo(n):
    c=0
    d=2
    r=[]
    while n>c:
        c1=0
        for i in range(2,d+1,1):
            if d%i==0:
                c1=c1+1
        if c1==1:
            r.append(d)
        d+=1
        c=len(r)
    return r

def serie(n):
    c=1
    res=[]
    d=0
    while n+1>c:
        d+=c
        res.append(str(d))
        c+=1
    return res


n=int(input())
a,b=primo(n),serie(n)
for i in range(0,n,1):
    if i%2!=0:
        print(str(a[i])+"/"+str(b[i]))
    else:
        print(str(b[i])+"/"+str(a[i]))
