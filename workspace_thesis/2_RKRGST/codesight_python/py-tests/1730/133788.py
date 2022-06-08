import math
a=int(input(""))
b=int(math.log10(a))
c=pow(10,b)
m=a
s=0
while s<>1: 
    s=0
    for j in range(b):
        c=pow(10,b)
        n=int(m/c)
        s=s+n*n
        m=m%c
        b=b-1
    s=s+m*m
    b=int(math.log10(s))
    c=pow(10,b)
    m=s

print(s)
