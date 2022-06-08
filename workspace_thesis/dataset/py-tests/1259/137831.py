import math
w=0
while w==0:
    a, n=map(int, input().split())
    l=math.log(n,a)
    l=l+0.01
    l=int(l)
    print(l) 