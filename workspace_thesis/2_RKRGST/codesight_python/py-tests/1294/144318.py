casos = int(input())
for i in range(casos):
	m, a, b = map(int, input().split())
	l = input().split()
	s = 0
	for j in l[a:b+1:]:
		s += int(j)
	print(s)