# 1096 puntos

m, n = list(map(int, input().rstrip().split()))
dic = {}
for i in range(m):
	key, value = input().split()
	dic[key] = value
for i in range(n):
	salario = 0
	while True:
		p = input()
		if p == '.':
			break
		p = p.split()
		for j in p:
			if j in dic.keys():
				salario += int(dic[j])
	print(salario)
