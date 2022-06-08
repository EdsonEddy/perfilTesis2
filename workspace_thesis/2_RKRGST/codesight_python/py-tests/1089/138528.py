import math
n=int(input())
c=int(math.log10(n))+1
if c%2==0:
    print("*")
else:
    c=c//2
    while c>0:
        n=n//10
        c=c-1
    print(n%10)