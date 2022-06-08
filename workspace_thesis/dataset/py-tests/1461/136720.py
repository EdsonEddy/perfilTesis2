s=int(input())
for s in range(s):
	n=str(input())
	if len(n)==1 and int(n)==1:
		print("Feliz")
		continue
	else:
		if len(n)==1:
			n=str(int(n)**2)
		else:
			n=n
		while len(n)!=1:
			n=list(n)
			n=[int(i) for i in n]
			g=0
			for u in n:
				g=g+int(u)**2
				n=str(g)
	if int(n)==1:
		print("Feliz")
	else:
		print("Triste")