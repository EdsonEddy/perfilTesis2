import math
for k in range(2):
    a=int(input(""))
    b=int(math.log10(a))
    m=a
    y=0
    for j in range(b):
        c=pow(10,b)
        n=int(m/c)
        if n%2==0:
            y=y+n 
        m=m%c
        b=b-1
    n=m%c
    if n%2==0:
        y=y+n
    print (y)