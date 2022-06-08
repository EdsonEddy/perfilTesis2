t=int(input( ))
for i in range(t):
	x=int(input( ))
	y=x
	p=1
	b=0
	while y>0:
		c=y%10
		y=y//10
		if c==2 or c==3 or c==5 or c==7:
			b=c*p+b
			p=p*10
	if b>0:
		print(b)
	else:
		print("-1")