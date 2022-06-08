while True:
	x=input()
	if x!="":
		x=int(x)
		for i in range (x):
			a=int(input())
			s=0
			while (a!=1 and a!=89):
				while (a>0):
					r=int(a%10)
					s=int((r*r)+s)
					a=a//10
				a=s
				s=0
			if a==1:
				print("Feliz")
			else:
				print("Triste")
	else:
		break