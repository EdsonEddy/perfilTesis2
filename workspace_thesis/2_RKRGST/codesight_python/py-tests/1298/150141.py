import sys
for line in sys.stdin:
	print(' '.join(str(e) for e in reversed([int(x) for x in line.split()][1:])))