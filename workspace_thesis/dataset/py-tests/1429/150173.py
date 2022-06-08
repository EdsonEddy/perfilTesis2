import sys
f = lambda n, b : (n | 2**b, n ^ 2**b)
for line in sys.stdin:
	print(*f(*[int(x) for x in line.split()]))