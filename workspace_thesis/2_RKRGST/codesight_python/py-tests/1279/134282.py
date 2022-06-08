while True:
	try:
		n,b = input().split()
		n,b=int(n),str(b)
	except:
		break
	cont=int(len(b))
	if n>=26:
		n=n%26
	l=""
	for i in range(cont):
		au=ord(b[i])
		if au>96 and au<123:
			au=au+n
			x=str(au)
			x=len(x)
			while (au>122):
				
				au=au-26
			l=l+chr(au)
		elif au==95:
			l=l+" "
		else:
			l=l+b[i]
	print(l.upper())