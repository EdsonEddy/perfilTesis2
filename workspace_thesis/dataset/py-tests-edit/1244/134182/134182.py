from math import pi
n=int(input())
for i in range(n):
    a=str(input())
    x=len(a)
    c=a.count("c")
    if c==1:
        a,b,c=a.split()
        r=float(b)*float(c)
    if c==2:
        a,b=a.split()
        r=pi*(float(b)**2)
    print("{0:.2f}".format(r))