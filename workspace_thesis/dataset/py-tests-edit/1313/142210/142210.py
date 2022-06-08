import sys
for n in sys.stdin:
	n=int(n)
	x=list(map(int,input().split()))
	v=[]
	for i in range(n):
		v.append(x[i])
	v.sort ()
	y=n
	a=0
	for i in range(n):
		t=v[i]*y
		y=y-1
		if (t>a):
			a=t
	print(a) 