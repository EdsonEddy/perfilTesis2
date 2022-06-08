n=int(input())
for i in range(n):
	s=str(input())
	d=len(s)
	r=""
	for g in range(d-1,-1,-1):
		r+=s[g]
	print(r)