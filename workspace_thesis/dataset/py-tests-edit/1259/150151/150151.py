import math
import sys
for line in sys.stdin:
	a, n = line.split()
	a, n = int(a), int(n)
	print(math.trunc(math.log10(n)/math.log10(a)))