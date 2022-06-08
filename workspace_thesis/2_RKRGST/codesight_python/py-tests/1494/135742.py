while 1:
	e,x=map(int,input().split())
	a,b=1,0
	c,d=2,3
	np=e
	s=0
	p=2
	for i in range(e):
		f=a+b
		a,b=b,f
		bb=1
		while bb>0:
			for j in range(2,p,1):
				if p%j == 0:
					y='no primo'
					break
			else:
				y='primo'
		
			if y =='primo':
				bb-=1
				s=s+(f/(p*x))
			p=p+1
	print('{0:.2f}'.format(s))