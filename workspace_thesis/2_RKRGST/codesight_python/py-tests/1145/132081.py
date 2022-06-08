y=int(input())
for j in range(1,y+1,1):
	x=int(input())
	a=-1
	b=1
	s=0
	c=a+b
	a=b
	b=c
	s=s+c
	for i in range(1,x+1,1):
		c=a+b
		a=b
		b=c
		s=s+c
	print(c)