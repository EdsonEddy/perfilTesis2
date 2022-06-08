casos = int(input())
for line in range(casos):
	n = int(input())
	d = list(map(int, input().split()))
	if n <= 1000000:
		c = 0
		for i in range(1, n-1):
			if d[i-1] < d[i] and d[i] > d[i+1]:
				c += 1
				i += 1
		print(c)