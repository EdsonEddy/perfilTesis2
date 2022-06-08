import math
n,k = map(int,input().split())
x = 0
y = 0

if n >= 1 and n<=1*10**18:
    c=int(math.log10(n))+1
    k=int(c-k)
    for i in range (1,k+2):
        d=n%10
        nn=n//10
        n=nn
        i+=1
print (c,d)