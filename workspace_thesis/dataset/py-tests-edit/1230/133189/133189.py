n=int(input())
h=int(n/3600)
hs=h*3600
m1=int(n/60)
m=m1%60
ms=m*60
s=n-(hs+ms)
print(h, m, s)
