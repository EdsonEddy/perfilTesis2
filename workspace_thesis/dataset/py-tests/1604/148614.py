def bases(x,y):
	a=0
	c=0
	while x != 0:
		d=x%10
		x=int(x/10)
		a=a+(d*(y**c))
		c=c+1
	return(a)

s=0
while s == 0:
	n=list(map(str,input().split()))
	if n =="":
		s=1
	if s ==0:
		for i in range(0, 2):
			a=int(n[0])
			b=int(n[1])
		x=bases(a,b)
		print(x)