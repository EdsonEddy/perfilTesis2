n=int(input())

def posicion(n):
    i=1
    a=0
    b=1
    c=a+b
    z=2
    while(i<=n):
        if(i%2==1):
            print (c)
            c=a+b
            a=b
            b=c
            i=i+1
        else:
            print(z)
            z=z+2
            i=i+1
    return
p=posicion(n)