while True:
	n=input()
	if n!="":
		n=int(n)
		un=["","unu","du","tri","kvar","Kvin","ses","Sep","OK","Nau"]
		if n%10==0:
			a=(n//10)
			if a==1:
				a=a-1
			print(un[a]+"dek")
		elif n>9:
			a=(n//10)
			if a==1:
				a=a-1
			print(un[a]+"dek",un[n%10])
		else:
			print(un[n])
	else:
		break