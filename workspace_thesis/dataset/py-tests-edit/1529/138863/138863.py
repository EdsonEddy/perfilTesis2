import math
a=int(input())
for i in range(a):
    n,c=map(int,input().split())
    cd=int(math.log(n,10)+1)
    for i in range(1,c+1):
        d=n//(10**(cd-1))
        n=n%10**(cd-1)
        n=n*10+d
    print (n)  