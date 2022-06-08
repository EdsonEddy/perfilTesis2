import math
x=int(input())
cd=int(math.log10(x))+1
y=(cd//2)+1
if (cd%2==1):
    for i in range (1,y+1):
        d=x%10
        x=x//10
    print(d)
else:
    print("*")
    
