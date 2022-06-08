pow = lambda a, b: a**b 
for _ in range(int(input())):
	print(pow(*[int(x) for x in input().split()]))