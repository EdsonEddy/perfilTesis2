n=0
while (n!=" "):
	n=int(input())
	a=-1
	b=1
	for i in range(0,n+1,1):
		c=a+b
		a=b
		b=c
	print(c)