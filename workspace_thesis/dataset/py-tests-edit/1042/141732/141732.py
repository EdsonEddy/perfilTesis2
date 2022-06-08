# 1042: Impuesto al carro más largo
c = int(input())
for i in range(c):
	m, n = list(map(float, input().rstrip().split()))
	print("{0:.3f}".format(m*n))