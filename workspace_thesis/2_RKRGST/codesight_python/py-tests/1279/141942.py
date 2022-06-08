while True:
	try:
		n,b = input().split()
		n,b=int(n),str(b)
	except:
		break
	if n>=26:
		n=n%26
	l=""
	for i in range(len(b)):
		au=ord(b[i])
		if au>96 and au<123:
			au=au+n
			while (au>122):
				au=au-26
			l=l+chr(au)
		elif au==95:
			l=l+" "
		else:
			l=l+b[i]
	print(l.upper())