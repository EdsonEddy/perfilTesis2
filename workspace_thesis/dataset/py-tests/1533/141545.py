from sys import *
for line in stdin:
	n,k=map(int,line.split())
	if (n+1)//2<k:
		print(2*(k-(n+1)//2))
	else:
		print(2*k-1)