from sys import stdin
import math

def cambio(n):
	a=n
	l=int(math.log10(n))
	nw=0
	p=l
	for i in range(1,l+2,1):
		d=n%10
		n=n//10
		nw=(d*(10**p))+nw
		p=p-1
	if(nw==a):
		return True
	else:
		return False
for x in stdin:
	x=int(x)
	c=0
	for j in range(1,x+1,1):
		n=int(input())
		if(cambio(n)):
			c=c+1
	print(c)