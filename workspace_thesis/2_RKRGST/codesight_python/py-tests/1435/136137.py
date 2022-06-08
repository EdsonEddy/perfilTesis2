import math
n,k = map(int,input().split())
#n=int(input())
#k=int(input())
x= cd = int(math.log10(n))+1
c=0
while n>0:
	dig = n//(10**(cd-1))
	c=c+1
	if c==k:
		print(x,dig)
		break
	n=n%(10**(cd-1))
	cd=cd-1