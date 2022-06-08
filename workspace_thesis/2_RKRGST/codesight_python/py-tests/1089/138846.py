import math
n=int(input())
cd=int(math.log(n,10)+1)
if cd%2==1:
    for i in range(0,int(cd/2)+1):
        d=n%10
        n=n//10
    print(d)    
else:
    print("*") 