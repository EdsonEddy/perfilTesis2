def epicentro(n):
    f=n
    c1=0
    c2=0
    while (f>0):
        f=f//10
        c1=c1+1
    if (c1%2==0):
        return ("*")
    else:
        while (c2<((c1//2)+1)):
            d=n%10
            n=n//10
            c2=c2+1
        return d
n=int(input())        
print(epicentro(n))    