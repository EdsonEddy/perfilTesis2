import sys
import math
for x in sys.stdin:
	n, k  =map(int,x.split())
	cd=int(math.log10(n))+1
	k=cd-k
	c=0
	print(cd,end=' ')
	while(n>0):
		if c==k:
			print(n%10)
		c=c+1
		n=n//10

