while 1:
	n=int(input())
	e,s=0,0
	while 1:
		s=s+2**e
		if s>=n:
			break
		e+=1
	print(e+1)