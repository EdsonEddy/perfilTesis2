import math
a=int(input())
b=int(math.log(a,10))
m=a
cont=1
while b>=0:
    c=pow(10,b)
    n=int(m/c)
    m=m%c
    if n==7 or n==4:
        b=b-1
    else:    
        cont=0
        b=-1
if cont==1:
    print("S")
else:
    print("N")