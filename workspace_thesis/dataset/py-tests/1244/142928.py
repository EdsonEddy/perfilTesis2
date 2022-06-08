from math import pi
n=int(input())
for i in range (n):
    x=input().split()
    sw=0
    area=1
    for j in (x):
        if sw==0:
            if j=='rectangle':
                sw=1
            else:
                sw=2
        else:
            if sw==1:
                area=area*float(j)
            else:
                area=pi*(float(j)**2)
    print("{0:.2f}".format(area))

F
while 1>0:
    f,x=input().split()
    k=int(f)
    abc="abcdefghijklmnopqrstuvwxyz"
    nc=""
    for i in x:
        letra=i
        if letra in abc:
            nc=nc+abc[(abc.index(letra)+k)%(len(abc))].upper()
        else:
            if letra == "_":
                nc=nc+" "
            else:
                nc=nc+letra.upper()
    print(nc)
