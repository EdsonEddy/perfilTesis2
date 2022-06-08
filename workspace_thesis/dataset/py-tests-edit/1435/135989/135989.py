import math
n,k=map(int,input().split())
c,d=0,0
if n>=1 and n<=1*10**18:
	c=math.log10(n)
	c=int(c+1)
	if k<=c:
		k=c-k
		for i in range(1,k+2):
			d=n%10
			nn=n//10
			n=nn
			i+=1
print(c,d)