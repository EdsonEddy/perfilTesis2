m=int(input())
for i in range(1,m+1):
	x=int(input())
	a=bin(x)
	c=a.count('11')
	print(c)