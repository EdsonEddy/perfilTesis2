from math import *
a,b,c=map(int,input().split())
if a!=0:
	ta=int(log10(a))+1
else:
	ta=1
if b!=0:
	tb=int(log10(b))+1
else:
	tb=1
if c!=0:
	tc=int(log10(c))+1
else:
	tc=1

ta=10**ta
tb=10**tb
tc=10**tc

res,may=0,0
res=(a*tb+b)*tc+c
if res>may:
	may=res
res=(a*tc+c)*tb+b
if res>may:
	may=res
res=(b*ta+a)*tc+c
if res>may:
	may=res
res=(b*tc+c)*ta+a
if res>may:
	may=res
res=(c*ta+a)*tb+b
if res>may:
	may=res
res=(c*tb+b)*ta+a
if res>may:
	may=res
print(may)
