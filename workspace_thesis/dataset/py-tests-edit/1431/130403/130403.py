from sys import stdin
for l in stdin:
	n,m,a,b=map(int,l.split())
	if n==1:
		print(a%m)
	elif n==2:
		print(b%m)
	else:
		c=0
		for i in range(1,n-1):
			c=(a%m+b%m)%m
			a=b
			b=c
		print(c)