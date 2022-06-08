import math
n=int(input())
for i in range (n):
    n1, n2 = map( int, input().split() )
    a=max(n1,n2)
    b=min(n1,n2)
    while b!=0:
        res= b
        b=a%b
        a=res
    print(res)