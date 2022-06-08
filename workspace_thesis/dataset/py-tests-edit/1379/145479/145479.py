while True:
	n=int(input())
	if n!=0:
		re=""
		s=tuple(input().split())
		r=[]
		for a in s:
			r.append(a)
		r.sort(reverse=True)
		d=len(r)
		for i in range(0,d,1):
			re=re+str(r[i])
		print(re)