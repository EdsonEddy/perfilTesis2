import sys
for line in sys.stdin:
	s = ''
	for x in sorted(line):
		if x != '\n':
			s += x
	print(s)
		