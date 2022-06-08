while True:
	x=input()
	if x!="":
		x=int(x)
		for i in range(x):
			a,b=input().split()
			l=list(map(int,input().split()))
			a,b=int(a),int(b)
			s=sum(l[a:b+1])
			print(s)
	else:
		break