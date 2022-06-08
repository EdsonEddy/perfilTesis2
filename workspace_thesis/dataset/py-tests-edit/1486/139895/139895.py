def par(n):
    global p
    q=p*2
    
    return q

def fibo (n):
    global a,b
    c=a+b
    return (c)

p=1
a=1
b=0
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print (par(n))
        p=p+1
    else:
        c=fibo(n)
        print (c)
        a=b
        b=c