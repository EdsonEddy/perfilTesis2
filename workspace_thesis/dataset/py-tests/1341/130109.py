import sys
while True:
	x=input()
	if x!="":
		x=int(x)
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
	else:
		sys.exit()