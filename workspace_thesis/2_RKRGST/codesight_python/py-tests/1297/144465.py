x=int(input())
x1=1
while x1<=x:
    n=input()
    m=''
    n1=1
    n2=len(n)
    p1=n2-1
    while n1<=n2:
        p=n[p1]
        m += p
        p1=p1-1
        n1=n1+1
    x1=x1+1
    print(m)