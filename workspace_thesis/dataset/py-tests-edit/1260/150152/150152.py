mcd = lambda a, b: a if b == 0 else mcd(b, a%b) 
for _ in range(int(input())):
	print(mcd(*[int(x) for x in input().split()]))