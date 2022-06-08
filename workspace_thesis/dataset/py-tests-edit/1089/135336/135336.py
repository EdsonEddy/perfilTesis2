import math
n = int(input())
c = 0
w = int(math.log(n,10))
if w%2==0:
    w=w+1
    y=(w//2)+1
    e =int(math.log(n,10)+1)
    while c<y:
        z=n//(pow(10,(e-1)))
        n=n%pow(10,(e-1))
        c =c+1
        e=e-1
    print (z)
else:
    print("*")