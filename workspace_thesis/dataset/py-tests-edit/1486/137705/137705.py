n=(int(input()))
p=2
a=-1 ; b=1
c= a+b
i=1
while i<=n:
    if i%2==0:
        print (p)
        p=p+2
        i += 1
    else:
        a=b
        b=c
        c = a+b
        print (c)
        i += 1