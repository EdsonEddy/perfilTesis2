t = int(input())
for _ in range(0, t):
	v = [int(x) for x in input().split()]
	c = 0
	for i in range(1, len(v)):
		if v[i-1] < v[i]:
			c += 1
	print(c)