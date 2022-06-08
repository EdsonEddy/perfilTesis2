while 1:
	n=int(input())
	for i in range(n):
		e=int(input())
		nn=e
		c=0
		while 1:
			r=0
			while nn>0:
				ud=nn%10
				r=r+ud**2
				nn=nn//10
			if 145==r:
				c+=1
				
			if r==1:
				rr='Feliz'
				break
			elif r==e or c>1:
				rr='Triste'
				break
			else:
				nn=r
		print(rr)