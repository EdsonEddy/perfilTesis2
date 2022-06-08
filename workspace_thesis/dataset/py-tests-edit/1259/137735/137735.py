import math
a,n=map(int,input().split())
while n!="" \
    "":
    if a==10:
        print(int(math.log10(n)))
    else:
        print(int(math.log(n,a)))
    a,n = map(int, input().split())