m,mo,a,b=map(int,input().split())
s=0
if m==1:
    print(a)
else:
    if m==2 :
        print(b)
    else:
        m=m-2
        for i in range(m):
            s=a+b
            a=b
            b=s
        b=b%mo
        print(b)