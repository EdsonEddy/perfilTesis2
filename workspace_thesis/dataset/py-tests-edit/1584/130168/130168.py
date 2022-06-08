while True:
	x=input()
	if x!="":
		x=int(x)
		entrada = [int(x) for x in input(). split ()]
		v=entrada[:]
		men=v[0]
		may=v[0]
		for i in range(x):
			if men>=v[i]:
				men=v[i]
			if may<=v[i]:
				may=v[i]
		print(may-men)
	else:
		break