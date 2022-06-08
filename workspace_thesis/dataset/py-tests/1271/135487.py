import math
n=int(input())
for j in range(n):
    x=int(input())
    z=x
    t=0
    a=x
    while x>0:
        d=x%10
        #print("d",d)
        x=x//10
        s=math.factorial(d)
        #while c!=(d+1):
            #s=s*c
            #c=c+1
            #print("s",s,c)
        t=s+t
    if(t==z):
        print("Y")
    else:
        print("N")