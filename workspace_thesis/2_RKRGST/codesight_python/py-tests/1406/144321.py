from sys import stdin
for line in stdin:
	v = list(map(int, input().split()))
	nu = list(map(int, input().split()))
	p = (sum(v) + sum(nu))/int(line)
	c = 0
	for i in range(int(line)):
		if v[i] + nu[i] < p:
			c += 1
	print(c)