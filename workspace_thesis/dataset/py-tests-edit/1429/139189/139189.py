import sys
import math
for x in sys.stdin:
	a, b = map(int,x.split())
	print(a|(1<<b),a^(1<<b))
