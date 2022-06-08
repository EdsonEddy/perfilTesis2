import math 
n=int(input())
cd=int(math.log(n,10))
if cd%2==0:
    a=int(cd/2)+1
    for i in range(1,a+1):
            d=n%10
            #print(d)
            n=int(n/10)
    print(d)        
else:
    print("*")
