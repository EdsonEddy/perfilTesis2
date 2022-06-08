n=0
while n!="":
	n,x=map(int,input().split())
	p=[2,3,5,7,11,13,17]
	a,b=1,0
	u,k,g=-1,0,2
	s=0
	for i in range(0,n,1):
		c=a+b
		a,b=b,c
		t=u+k+g
		u,k,g=k,g,t
		v=t*(x**p[i])/c
		if i==0 or i%2==0:
			s=s+v
		else:
			s=s-v
	print("{0:.2f}".format(s))