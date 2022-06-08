x=int(input())
for i in range(x):
	aa=int(input())
	entrada = [int(x) for x in input(). split ()]
	v=entrada[:]
	for i in range(aa):
		if i==0:
			s=v[i]
		else:
			o=s*v[i]
			while s!=v[i]:
				if v[i]>s:
					v[i]=v[i]-s
				else:
					s=s-v[i]
			mc=v[i]
			s=int(o/mc)
	print(s)