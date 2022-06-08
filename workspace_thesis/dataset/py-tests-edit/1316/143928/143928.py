import sys
for line in sys.stdin:
	v1 = sorted([int(x) for x in input().split()])
	v2 = list(reversed(sorted([int(x) for x in input().split()])))
	s = 0
	for x, y in zip(v1, v2):
		s += x*y;
	print(s)
