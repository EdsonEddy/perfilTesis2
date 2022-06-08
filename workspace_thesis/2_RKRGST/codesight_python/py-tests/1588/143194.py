while True:
	x=input()
	if x!="":
		x=int(x)
		for u in range(x):
			cant=int(input())
			s=0
			entrada = [int (y) for y in input(). split ()]
			v=entrada[:]
			for i in range(cant):
				if (v[i]*2)%3==0:
					s=s+v[i]*2
			print("La suma es",s)
	else:
		break