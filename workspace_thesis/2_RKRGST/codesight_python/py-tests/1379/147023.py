while True:
	n=int(input())
	if n!=0:
		x=input().split()
		x.sort()
		s=""
		for i in range(len(x)):
			s=x[i]+s
		print(s)
	else:
		break