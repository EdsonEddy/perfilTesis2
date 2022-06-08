while True:
	n,a,b=map(int,input().split())
	r=0
	for i in range(1,n+1,1):
		s=0
		for j in str(i):
			s+=int(j)
		if s>=a and s<=b:
			r+=i
	print(r)