while True:
	n=int(input())
	x=input().split()
	y=input().split()
	s=0
	c=0
	for i in range(n):
		s=s+int(x[i])+int(y[i])
	s=s/n
	for i in range(n):
		if (int(x[i])+int(y[i]))<s:
			c+=1
	print(c)