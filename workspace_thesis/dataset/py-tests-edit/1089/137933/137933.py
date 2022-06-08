import math

def medio(n):
    n=int(n)
    cd=int(math.log10(n))+1
    r=0
    c=1
    while (True):
        if (c==(cd//2)+1):
            r=n%10
            break
        n=n//10
        c=c+1
    return (r)

n=int(input())
r1=0
cd1=int(math.log10(n))+1
if (cd1%2!=0):
    r1=medio(n)
    print(r1)
else:
    print("*")
