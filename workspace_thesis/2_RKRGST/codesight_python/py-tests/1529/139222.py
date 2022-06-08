import math
t=int(input())
for i in range(t):
	x,n=map(int,input().split())
	c=int(math.log10(x))
	for j in range(n):
		d=x//(10**c)
		x=(x%(10**c))*10+d
	print(x)