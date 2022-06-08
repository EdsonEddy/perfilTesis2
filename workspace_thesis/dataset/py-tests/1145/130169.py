num=int(input())
for i in range(num):
	x=int(input())
	a=1
	b=0
	c=0
	cc=1
	while(cc<=x):
		c=a+b
		a=b
		b=c
		cc=cc+1		
	print(c)