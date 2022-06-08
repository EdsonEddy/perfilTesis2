from sys import stdin
def lee(n,s):
	v=s.split(" ")
	c=0
	for i in range(0,n,1):
		if (v[n-1]==v[i]):
			c=c+1
	return c
for n in stdin:
	x=0
	n=int(n)
	s=input()
	x=lee(n,s)
	print(x)