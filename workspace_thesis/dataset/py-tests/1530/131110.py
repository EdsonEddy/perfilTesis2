x=int(input())
for i in range (x):
	n=int(input())
	nn=0
	ccc=0
	while n>0:
		aux=n%10
		cc=0
		v=1
		while (v<=aux):	
			if aux%v==0:
				cc=cc+1
			v=v+1
		n=int(n/10)
		if cc==2 and aux!=1:
			nn=nn+aux*10**ccc
			ccc=ccc+1
	print(nn)