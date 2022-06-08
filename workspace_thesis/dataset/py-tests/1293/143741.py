while 1:
	n=int(input())
	for i in range(n):
		a,b=map(int,input().split())
		c=input().split()
		lc=list(c)
		s=0
		for j in range(a,b+1,1):
			s=s+int(lc[j])
		print(s)