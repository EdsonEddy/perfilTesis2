while True:
	x=input()
	if x!=""  and x!="0":
		x=int(x)
		l=list(map(int,input().split()))
		n=l[x-1]
		c=l.count(n)
		print(c)
	else:
		break