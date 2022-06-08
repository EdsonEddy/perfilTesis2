import math
n=int(input())
c=int(math.log10(n))+1
t=(c//2)+1
k=0
cont=0
while(cont<=t):
    d=n%10
    n=n//10
    cont=cont+1
    if(cont==t and cont%2!=0):
        k=1
        v=d
        break
if(k==1):
    print(v)
else:
    print("*")