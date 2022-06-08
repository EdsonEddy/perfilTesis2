n=int(input())
for i in range(n):
	x=input().split()
	c=-1
	m=0
	for j in x:
		d=int(j)
		if d>m:
			c=c+1
		m=d
	print(c)