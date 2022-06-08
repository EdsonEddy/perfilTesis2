while True:
	s=list(input().split())
	r=""
	d=int(s[0])
	for i in range(d,0,-1):
		r=r+" "+str(s[i])
	print(r[1:])