from math import pi
c=int(input())
while c > 0:
    c-=1
    m=str(input())
    l=m.split(' ')
    if len(l)==3:
        f=str(l[0])
        p=float(l[1])
        s=float(l[2])
    if len(l)==2:
        f = str(l[0])
        p = float(l[1])
    if f == 'rectangle':
        p,s=float(p),float(s)
        ar=p*s
        print('%.2f'%ar)
    elif f == 'circle':
        p=float(p)
        s=0
        ac=pi*p**2
        print('%.2f'%ac)
