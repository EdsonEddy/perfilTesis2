t = int(input())
for _ in range(0, t):
	n = int(input())
	v = [int(x) for x in input().split()]
	for x in list(reversed(v)):
		print(x, end=' ')
	print()
