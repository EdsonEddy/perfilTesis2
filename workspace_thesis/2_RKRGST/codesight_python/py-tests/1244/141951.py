while True:
	x=input()
	if x!="":
		x=int(x)
		for i in range(x):
			entrada = [y for y in input(). split ()]
			v=entrada[:]
			if v[0]=="circle":
				ar=(float(v[1])**2)*3.141592653589793
				print("%.2f" % ar)
			else:
				ar=float(v[1])*float(v[2])
				print("%.2f" % ar)
	else:
		break