x=int(input())
for i in range(x):
	n, a, b = [int(x) for x in input(). split ()]
	contador = 0
	for i in range(n, a, b + 1):
		if i % 2 == 0:
			contador += 1
	n,a,b=int(n),int(a),int(b)
	l=list(map(int,input().split()))
	a,b=int(a),int(b)
	s=sum(l[a:b+1])
	print(s)