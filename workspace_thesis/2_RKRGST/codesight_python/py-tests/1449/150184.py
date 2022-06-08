import sys
for line in sys.stdin:
	a, b = [int(x) for x in line.split()]
	input()
	s = 0
	for x in [int(x) for x in input().split()]:
		if a <= x <= b:
			s += x
	print(s)