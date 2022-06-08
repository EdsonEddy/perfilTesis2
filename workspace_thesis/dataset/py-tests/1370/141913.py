while True:
	x=input()
	if x!="":
		x=int(x)
		if x==0:
			print(0)
		else:
			co=bin(x)
			co=co[2:]
			print(len(co))
	else:
		break