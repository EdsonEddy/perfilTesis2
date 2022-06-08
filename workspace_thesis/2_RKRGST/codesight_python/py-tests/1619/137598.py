while 1:
	a,b=map(int,input().split())
	s=a+b
	r=a-b
	p=a*b
	max=s
	if s>r:
		if s>p:
			print(s)
		else:
			print(p)
	elif r>p:
		print(r)
	else:
		print(p)