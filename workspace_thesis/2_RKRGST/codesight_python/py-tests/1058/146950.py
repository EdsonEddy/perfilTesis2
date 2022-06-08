n=int(input())
for i in range(n):
	x=int(input())
	z=input()
	r=z.split()
	for k in range(x):
		r[k]=int(r[k])
	m=sorted(r)
	print(*m)