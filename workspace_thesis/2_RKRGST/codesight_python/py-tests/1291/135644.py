while 1:
	l=input().split()
	ll=len(l)
	s=0
	for i in range(ll):
		if int(l[i]) != 0:
			s+=int(l[i])
		else:
			break
	print(s)