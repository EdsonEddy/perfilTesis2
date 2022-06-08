while 1:
	n =int(input())
	for j in range(n):
		m,a,b=map(int,input().split())
		c=input().split()
		s=0
		for k in range(a,b+1,1):
			s=s+int(c[k])
		print(s)