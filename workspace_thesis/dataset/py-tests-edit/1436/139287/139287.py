from math import *
def tamN(n):
    tam=0
    if n!=0:
        tam=int(log10(n))+1
    else:
        tam=1
    return tam
def comp(a,b,c,ta,tb,tc):
    r=(a*tb+b)*tc+c
    return r
a,b,c=map(int,input().split())
ta,tb,tc=0,0,0
ta = tamN(a)
tb = tamN(b)
tc = tamN(c)
ta=10**ta
tb=10**tb
tc=10**tc

may,r=0,0
r=comp(a,b,c,ta,tb,tc)
if r>may:
    may=r
r=comp(a,c,b,ta,tc,tb)
if r>may:
    may=r
r=comp(b,a,c,tb,ta,tc)
if r>may:
    may=r
r=comp(b,c,a,tb,tc,ta)
if r>may:
    may=r
r=comp(c,a,b,tc,ta,tb)
if r>may:
    may=r
r=comp(c,b,a,tc,tb,ta)
if r>may:
    may=r
print(may)
