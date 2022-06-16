def invertir(x):
    num = int((str(x)[::-1]))
    return num
def unidad(x):
    su=0
    while x>0:
        mod=x%10
        x=x//10
        su+=mod
    return su
num=int(input())
for i in range(num):
    n,k=map(int,input().split())
    nn=""
    while n>10**(k-1)or n==10**(k-1):
        mod=n%(10**k)
        num=mod//10 
        n=n//10**k
        n= n*10**(k-1)+num
        #print(mod,end=" ")
        x=invertir(mod)
        #print(x,end=" ")
        while x>9:
            x=unidad(x)
        #print(x)
        nn=str(x)+nn
    print(nn)
