import math
n=int(input())
for j in range(n):
    x,y=map(int,input ().split())
    a=x
    p=0
    c=int(math.log10(x))
    while p<y:
        p+=1
        d=int(a/pow(10,c))
        a=(a%pow(10,c))
        a=a*10+d
    print(a)