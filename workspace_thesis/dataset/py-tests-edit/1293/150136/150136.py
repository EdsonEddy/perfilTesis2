for _ in range(int(input())):
	a, b = [int(x) for x in input().split()]
	print(sum([int(x) for x in input().split()][a:b+1]))