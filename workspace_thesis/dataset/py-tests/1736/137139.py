while 1:
	n=int(input())
	for i in range(n):
		e=2**i
		p=1+2**e
		if i !=n-1 :
			print(p,end=' ')
		else:
			print(p)