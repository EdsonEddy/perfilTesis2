import math
n,k= map(int,input().split())
c = int (math.log10 (n)) + 1
print(c,end=' ')
i=0
while n>0 :
    dig=n//(10**(c-1))
    i=i+1
    if (i==k):
        print(dig)
        break
    n=n%10**(c-1)
    c-=1
    
    
