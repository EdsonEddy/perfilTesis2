import sys
import math
for line in sys.stdin:
	print(1 + math.trunc(math.log10(int(line))/math.log10(2)))