import math
a=int(input(""))
b=int(math.log10(a))
c=10**b
m1=a
i=1
for j in range(b):
    n=a//c
    m=m1%10
    m1=m1//10
    if n==m:
        i=1
    else:
        i=0
        b=0
    a=a%c
    b=b-1
    c=10**b
if  i==1:
    print("S")
else:
    print("N")