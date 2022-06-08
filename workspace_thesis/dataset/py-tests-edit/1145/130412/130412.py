x=int(input())
for i in range(x):
	a,b,c=1,0,0
	y=int(input())
	for j in range(y):
		c=a+b
		a=b
		b=c
	print(c) 