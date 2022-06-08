while 1:
	v=[]
	r=[]
	n=int(input())
	b=2
	for i in range(n+1):
		v.append(b**i)
	lv=len(v)
	llv=lv
	d=0
	while llv>0:
		for j in range(d,lv):
			if j+1<lv:
				r.append( v[d]+v[j+1])
		d+=1
		llv-=1
	r.sort()
	for k in range(n):
		if k<n-1:
			print(r[k], end=' ')
		else:
			print(r[k])