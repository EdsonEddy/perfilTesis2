import math
n=int(input())
c=0
pot=int(math.log(n,10))
if pot%2==0:
    pot=pot+1
    epi=(pot//2)+1
    cd=int(math.log(n,10)+1)
    while c<epi:
        d=n//(pow(10,(cd-1)))
        n=n%pow(10,(cd-1))
        c=c+1
        cd=cd-1
    print(d)
else:
    print("*")