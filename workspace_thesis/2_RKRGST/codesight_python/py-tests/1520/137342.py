n=int(input())
n1=n*n
a=1
sf=0
while a!=n or sf!=n:
    if sf==n:
        a=a+1
        sf=1
    else:
        sf=sf+1
    num=str(a)
    den=str(sf)
    print(num+"/"+den)