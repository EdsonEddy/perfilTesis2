from sys import stdin
for line in stdin:
	n = int(line)
	l = input().split()
	c = 0
	for i in l:
		if i == l[n-1]:
			c += 1
	print(c)