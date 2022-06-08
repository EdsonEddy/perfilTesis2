n=0
while n!="":
	a=input().split()
	c=''
	for i in range(len(a)-1,0,-1):
		if i!=1:
			c=c+a[i]+" "
		else:
			c=c+a[i]
	print(c)