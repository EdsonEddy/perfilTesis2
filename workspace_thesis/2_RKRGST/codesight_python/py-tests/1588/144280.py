casos = int(input())
for i in range(casos):
	n = int(input())
	v = list(map(int, input().split()))
	s = 0
	for j in v:
		if j % 3 == 0:
			s += 2*j
	print('La suma es',s)