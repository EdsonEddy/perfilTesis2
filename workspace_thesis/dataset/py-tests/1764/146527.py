def abun(n):
    s=0
    for i in range(2,n,1):
        if n%i==0:
            s+=i
    return s

def feliz(n):
    d=str(n)
    sw=0
    q=len(d)
    while d!=n or d!=1 or q>1:
        s=0
        for a in d:
            s+=int(a)**2
        d=str(s)
        q=len(d)
        if q==1:
            break
    if d=="1":
        sw=1
    return sw

sa=0
sf=0
max = 0
min = 100
while True:
    n=int(input())
    if n!=-1:
        if n>max:
            max=n
        if n<min:
            min=n
        s=abun(n)
        if s>n:
            sa+=n
        g=feliz(n)
        if g==1:
            sf+=n
    else:
        print(max)
        print(min)
        print(sa)
        print(sf)
        break

