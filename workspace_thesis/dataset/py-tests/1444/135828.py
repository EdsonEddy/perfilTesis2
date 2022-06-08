while 1:
	k=int(input())
	for w in range (k):
		n=int(input())
		s=' '
		c=0
		while n>0:
			ud=n%2
			s=str(ud)+s
			n=n//2
		s=int(s)
		while s>0:
			ud=s%10
			s=s//10
			if ud==1:
				ud=s%10
				if ud==1:
					c+=1
					s=s//10		
		print(c)