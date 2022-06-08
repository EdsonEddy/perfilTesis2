while (True):
	a,b=input().split()
	a,b=int(a),int(b)
	if int(a)!=0 or int(b)!=0:
		s=int(0)
		aa=a
		entrada = [int(x) for x in input(). split ()]
		v=entrada[:]
		for i in range(aa):
			a=a-1
			s=s+(v[i]*(b**a))
		print(float(s))
		v.pop()
	else:
		break