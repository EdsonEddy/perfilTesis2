import sys
import math
for x in sys.stdin:
	a, b = map(int,x.split())
	c = (a+b)//a
	c = int(math.log(c)/math.log(2))
	print(c)
