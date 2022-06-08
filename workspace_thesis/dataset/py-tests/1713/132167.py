from sys import stdin
for n in stdin:
	n=int(n)
	s=0
	for j in range(1,n+1,1):
		x=int(input())
		s=s+x
	print(s)