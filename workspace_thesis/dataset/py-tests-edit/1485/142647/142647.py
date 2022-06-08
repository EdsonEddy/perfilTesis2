while True:	
	c=int(input())
	coc=0
	for i in range(c):
		n=int(input())
		g=n
		n=str(n)
		t=n[::-1]
		g=str(g)
		if t==g:
			coc=coc+1
	print(coc)
		
	
	