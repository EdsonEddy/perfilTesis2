import math
import sys
for i in sys.stdin:
	n = int(i)
	n = int(math.log(n)/math.log(2)) + 1
	print(n)
