while True:
	l=list(map(int,input().split()))
	if len(l)==0:
		break
	else:
		p=[2,3,5,7,11]
		f=[1,1,2,3,5]
		sw=[1,3,6,10,19]
		si=-1
		s=0
		for i in range(l[0]):
			si=si*-1
			s=(((l[1]**p[i])*sw[i])/f[i])*si+s
	print("%.*f"%(2,s))