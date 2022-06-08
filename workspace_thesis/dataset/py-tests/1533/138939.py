import sys
for x in sys.stdin:
	n, k=map(int,x.split())
	n=n+1
	if k<(n//2):
		print(2*k-1)
	else:
		print((k-(n//2))*2)

