while 1:
	n=int(input())
	d=0
	if n>0:
		for i in range(n):
			d=d*10+1
			if i!=n-1:
				print(d,end=' ')
			else:
				print(d)
	else:
		print('error')	