from math import*
def tamN(n):
    tam=0
    if n!=0:
        tam=int(log10(n))+1
    else:
        tam=1
    return tam
def comp(a,ta,b,tb,c,tc):
    r=(a*tb+b)*tc+c
    return r
a,b,c=map(int,input().split())
ta,tb,tc=0,0,0
ta=tamN(a)
tb=tamN(b)    
tc=tamN(c)

ta=10**ta
tb=10**tb
tc=10**tc
may,r=0,0
r=comp(a,ta,b,tb,c,tc)
may=max(r,may)
r=comp(a,ta,c,tc,b,tb)
may=max(r,may)
r=comp(b,tb,a,ta,c,tc)
may=max(r,may)
r=comp(b,tb,c,tc,a,ta)
may=max(r,may)
r=comp(c,tc,a,ta,b,tb)
may=max(r,may)
r=comp(c,tc,b,tb,a,ta)
may=max(r,may)
print(may)


