import math
m=int(input())
for i in range (1,m+1):
    n=int(input())
   
    y=n
    s=0
    
    while n>0:
        d=n%10
        n=n//10
        f=1
        for j in range (1,d+1,1):
            f=f*j
        s=s+f
    if (y==s):
        print("Y")
    else:
        print("N")
    
            

            
