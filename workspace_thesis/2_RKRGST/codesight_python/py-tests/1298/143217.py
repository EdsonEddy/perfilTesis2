while True:
	entrada = [int (y) for y in input(). split ()]
	v=entrada[:]
	if int(len(v))!=0:
		aux=v[0]
		if aux==0:
			print("")
		else:
			v.pop(0)
			v.reverse()
			print(*v)
	else:
		break