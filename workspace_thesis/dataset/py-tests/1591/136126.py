import math
n=int(input())

for i in range(n):
    s=0;c=0
    k=int(input())
    m=int(math.log10(k))
    for j in range(m+1):
        
        d=k%10
        if d==2 or d==3 or d==5 or d==7:
            c=c+1
            s=d*10**(c-1)+s
            
        k=k//10
    if s>0:
        print(s)
    else:
        print("-1")
   