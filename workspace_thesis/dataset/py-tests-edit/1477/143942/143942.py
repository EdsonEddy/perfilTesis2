n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
for x in sorted(list(set(a+b))):
	print(x)