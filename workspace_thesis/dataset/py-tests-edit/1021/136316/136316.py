from sys import *
for line in stdin:
	a,b=map(int,line.split())
	while a!=b:
		if a>b:
			a=(a>>1)
		else:
			b=(b>>1)
	print(a)
