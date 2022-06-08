def pri():
	con=2
	pp=[2]
	cont=3
	while con<=40:
		au=0
		for i in range(1,cont+1):
			if cont%i==0:
				au+=1
		if au==2:
			pp.append(cont)
			con+=1
		cont+=1
	return pp

def fi():
	a,b,con=1,0,1
	f=[]
	while con<=40:
		c=a+b
		a=b
		b=c
		f.append(c)
		con+=1
	return f
while True:
	l=list(map(int,input().split()))
	if len(l)==0:
		break
	else:
		p=pri()
		f=fi()
		s=0
		for i in range(l[0]):
			s=f[i]/(l[1]*p[i])+s
	print("%.*f"%(2,s))