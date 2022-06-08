n=int(input())
m=1
a=1
b=0
h=0
while m<=n:
    if m%2==1:
        r=a+b
        print(r)
        a=b
        b=r
        m+=1;
    else:
        h+=2
        print(h)
        m+=1