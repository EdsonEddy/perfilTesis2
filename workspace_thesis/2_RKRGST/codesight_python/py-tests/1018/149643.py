for _ in range(0, int(input())):
	x, y = [int(x) for x in input().split()]
	print('=' if x == y else ( '<' if x < y else '>' ))