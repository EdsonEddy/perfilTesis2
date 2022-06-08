import sys
n = int(input())
for i in range(n):
	a, b = map(int,input().split())
	c = 0
	if( a//3 > b//2):
		c = b//2
	else:
		c = a//3
	print("{:d} {:d}".format(c,((a-(3*c))+(b-(c*2)))))