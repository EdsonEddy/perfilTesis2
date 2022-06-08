import math
x=int(input(""))
for j in range(1,x+1,1):
    n=int(input(""))
    l=(int(math.log10(n)))+1
    p=0
    d=0
    a=0
    for i in range(1,l+1,1):
        d=n%10
        n=n//10
        if(d==2 or d==3 or d==5 or d==7):
            a=a+(d*(10**p))
            p=p+1
    print(a)