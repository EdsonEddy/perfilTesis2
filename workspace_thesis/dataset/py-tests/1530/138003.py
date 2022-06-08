import math
def imprime(k):
    if (d==2 or d==3 or d==5 or d==7):
        return True
    else:
        return False
n=int(input())
for i in range (1,n+1):
    x=int(input())
    cd=int(math.log10(x))
    y=0    
    while x>0:
        d=x//10**(cd)
        x=x%10**cd
        cd=cd-1
        flag=imprime(d)
        if (flag==True):
            y=y*10+d
    print(y)
