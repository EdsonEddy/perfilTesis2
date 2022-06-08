while 1:
	n=int(input())
	a=1
	b=0
	if n!=0:
		for i in range(n):
			a,b=b,a+b
			if i==n-1:
				print(b)
	else:
		print(b)