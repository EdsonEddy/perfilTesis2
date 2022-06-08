n, m, a, b = list(map(int, input().split()))
c = 0
for _ in range(2, n):
	c = (a%m + b%m)%m
	a = b
	b = c
print(c)