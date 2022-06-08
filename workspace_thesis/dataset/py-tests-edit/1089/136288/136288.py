from math import *
n=int(input())
if (n&1)==0:
	print("*")
else:
	cd=int(log10(n))+1
	cd=(cd>>1)
	while(cd>0):
		n//=10
		cd-=1
	print(n%10)
	