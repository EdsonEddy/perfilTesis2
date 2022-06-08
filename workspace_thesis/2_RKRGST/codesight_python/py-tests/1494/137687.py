import sys
primos=[]
fib=[]
def hallarPrimos(n):
    primos.extend([2,3,5,7,11,13,17,19,23])
    for i in range(27,n):
        for j in primos:
            if i%j==0:
                break
        else:
            primos.append(i)
def hallarFib(n):
    fib.extend([1,1])
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])

hallarPrimos(1000)
hallarFib(1000)
for linea in sys.stdin:
    n,x=map(int,linea.split())
    s=0
    for i in range(0,n):
        s=s+fib[i]/(primos[i]*x)
    print('{:.2f}'.format(s))