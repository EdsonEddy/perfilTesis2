while 1:
	e,x=map(int,input().split())
	a,b=1,0
	np=e
	s=0
	p=2
	m,n,o=2,1,3
	fl=1
	t=0
	for i in range(e):
		f=a+b
		a,b=b,f
		bb=1
		if fl==1:
			ns=1
			fl+=1
		elif fl==2:
			ns=3
			fl+=1
		else:
			ns=m+n+o
			m,n,o=n,o,ns
		while bb>0:
			for j in range(2,p,1):
				if p%j == 0:
					y='no primo'
					break
			else:
				y='primo'
		
			if y =='primo':
				bb-=1
				if t%2==0:
					s=s+ns*(x**p)/f
					t+=1
				else:
					s=s-ns*(x**p)/f
					t+=1
			p=p+1
	print('{0:.2f}'.format(s))