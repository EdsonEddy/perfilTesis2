w=0
c=0
cc=0
m=0
while w==0:
    t=float(input())
    if t==0:
        w=1
        break
    else:
        if t<0:
            c=c+1
        cc=cc+1
        if m<t:
            m=int(t)
porc=int(c*100/cc)
print(porc)
print(m)