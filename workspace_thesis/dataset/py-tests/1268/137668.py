while 1:
	c,p=map(int,input().split())
	if c>=1 and c<=50 and p>=1 and p<=50:
		if c==0 and p==0:
			break
		elif p%2 == 0:
			x=(p-2*c)//2
			y=(4*c-p)//2
			if x>=0 and y>=0:
				print(y,x)
			else:
				print(-1)
		else:
			print(-1)