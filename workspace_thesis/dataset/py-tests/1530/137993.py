import math
n=int(input())
for i in range(n):
    x=int(input())
    res=0
    po=int(math.log10(x))
    while (x != 0):
        dig=x//pow(10,po)
        x=x%pow(10,po)
        po-=1
        flag=True
        for j in range(2,dig):
            if(dig%j==0):
                flag=False
        if(dig<2):
            flag=False
        if(flag==True):
            res=res*10+dig
    print(res)
