from math import *
a,b,c=map(int,input().split())

ta,tb,tc=0,0,0
if a!=0:
    ta = int(log10(a))+1
else:
    ta = 1
if b!=0:
    tb = int(log10(b))+1
else:
    tb = 1
if c!=0:
    tc = int(log10(c))+1
else:
    tc = 1

ta = 10**ta
tb = 10**tb
tc = 10**tc

may,r= 0,0

r=(a*tb+b)*tc+c
if r>may:
    may=r
    
r =(a*tc+c)*tb+b
if r>may:
    may=r

r=(b*ta+a)*tc+c
if r>may:
    may=r

r=(b*tc+c)*ta+a
if r>may:
    may=r

r=(c*ta+a)*tb+b
if r>may:
    may=r

r=(c*tb+b)*ta+a
if r>may:
    may=r
print(may)
