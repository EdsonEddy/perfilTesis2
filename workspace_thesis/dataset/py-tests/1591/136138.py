import math
p=int(input())
for i in range(1,p+1):
    n=int(input())
    x=n
    cd=int(math.log10(n))
    y=0 
    while n>0:
        d=int(n/(math.pow(10,cd)))
        n=n%(math.pow(10,cd))
        cd=cd-1
        if d==2 or d==3 or d==5 or d==7:
            y=y*10+d 
    if y==0:
        print("-1")
    else:
        print(y)