n=int(input())
m=0
l=0
while n>0:
    x=n%10
    n=n//10
    x=x**2
    m=m+x
while m>0:
    x=m%10
    m=m//10
    x=x**2
    l=l+x
    if m==1:
        print(m)