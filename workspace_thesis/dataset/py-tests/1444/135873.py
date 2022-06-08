while True:
	x=input()
	if x!="":
		x=int(x)
		for i in range (x):
			a=int(input())
			a=bin(a)
			au=int(len(a))
			n=int(a[2:au])
			con=0
			pares=0
			conta=0
			while (n>0):
				conta+=1
				k=n%10
				if k==1:
					con+=1
				else:
					con=0
				if con==2:
					pares+=1
					con=0
				if n!=1:
					n=int(a[2:(au-conta)])
				else:
					n=int(0)
			print(pares)
	else:
		break