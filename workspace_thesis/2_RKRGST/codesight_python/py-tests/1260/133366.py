n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a > b:
        aux=b
        b=a
        a=aux
    c=1
    while c<=a:
        if a%c==0 and b%c==0:
            d=c
        c+=1 
    print(d)