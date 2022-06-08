n=int(input())
n1=n*n
c=1
sf=0
while c!=n or sf!=n:
    if sf==n:
        c=c+1
        sf=1
    else:
        sf=sf+1
    num=str(c)
    den=str(sf)
    print(num+"/"+den)