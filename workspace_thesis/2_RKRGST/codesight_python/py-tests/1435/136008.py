import math
n,k=map(int,input().split())
c=0
cd=int(math.log10(n))
x=cd+1
while k>0:
	d=n//(10**cd)
	n=n%(10**cd)
	cd=cd-1
	k=k-1
print(x, d)