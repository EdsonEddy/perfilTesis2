import sys
import math
for x in sys.stdin:
	a = int(x)
	print('{:.2f}'.format(math.sin(a*math.pi/180)))
