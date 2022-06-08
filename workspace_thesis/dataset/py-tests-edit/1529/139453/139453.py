import math
m=int(input())
for j in range (1,m+1):
    n,k=map(int,input().split())
    cd=int(math.log10(n))
    for i in range (1,k+1):
        d=n//10**cd
        n=n%10**cd
        n=n*10+d
    print(n)
