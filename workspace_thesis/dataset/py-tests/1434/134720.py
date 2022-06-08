import math
n=int(input())
m=n
c=0
while(n>0):
    c=(c*10)+(n%10)
    n=n//10
if(m==c):
    print ("S")
else:
    print ("N") 