while 6!=0:
	x,y,a,b=map(int,input().split())
	if a==00:
		a=24
	if b<y:
		a=a-1
		b=b+60
	o1=a-x
	o2=b-y
	print(o1,o2)