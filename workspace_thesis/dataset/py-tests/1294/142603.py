t = int(input())
for _ in range(0, t):
	m, a, b = [int(x) for x in input().split()] 
	v = [int(x) for x in input().split()]
	print(sum(v[a:b+1]))