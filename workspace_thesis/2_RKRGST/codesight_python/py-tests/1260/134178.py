from math import sqrt
n=int(input())
c=1
h=0
while c<=n:
    a,b=map(int,input().split())
   
    if a<b:
        aux=a
        a=b
        b=aux
    m=a%b
    while m!=0:
        a=b
        b=m
        h=m
        m=a%b
    c=c+1
    print (h)