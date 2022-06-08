import math
n=int(input())
a=0
mat=int(math.log(n,10))
if mat%2==0:
    mat=mat+1
    b=(mat//2)+1
    cd=int(math.log(n,10)+1)
    while a<b:
        d=n//(pow(10,(cd-1)))
        n=n%pow(10,(cd-1))
        a=a+1
        cd=cd-1
    print(d)
else:
    print("*")