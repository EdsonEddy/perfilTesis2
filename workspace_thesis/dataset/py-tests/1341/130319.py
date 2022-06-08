from sys import stdin
for l in stdin:
	x=int(l)
	a,b,c=-1,1,0
	for i in range(x+1):
		c=a+b
		a=b
		b=c
	print(c)