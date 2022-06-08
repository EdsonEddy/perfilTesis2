import sys
for n in sys.stdin:
	n=int(n)
	x=list(map(int,input().split()))
	v=[]
	for i in range(n):
		v.append(x[i])
	c=0
	for i in range(1,n-1,1):
		if (v[i-1]>v[i] <v[i+1] or v[i-1]<v[i] >v[i+1] ):
			c=c+1
	print(c)