import sys
for line in sys.stdin:
	n = int(line)
	v = [int(x) for x in input().split()]
	c = 0
	for i in range(1, len(v)-1):
		if v[i-1] > v[i] < v[i+1] or v[i-1] < v[i] > v[i+1]:
			c += 1
	print(c)
	