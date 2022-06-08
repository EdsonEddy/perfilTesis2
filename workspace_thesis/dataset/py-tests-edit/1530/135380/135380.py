import math
p=int(input())
for i in range(1,p+1,1):
    n=int(input())
    ct=int(math.log(n))
    w=0
    while n>0:
        d=n//(pow(10,ct))
        n=n%(pow(10,ct))
        ct=ct-1
        if d==2 or d==3 or d==5 or d==7:
            w=(w*10)+d
    print(w)
