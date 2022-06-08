import sys
for x in sys.stdin:
	A = [int(i) for i in x.split()]
	print(sum(A))	