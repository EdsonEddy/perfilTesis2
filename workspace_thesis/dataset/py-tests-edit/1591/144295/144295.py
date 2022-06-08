casos = int(input())
p = ['2', '3', '5', '7']
for i in range(casos):
	n = input()
	nP = ''
	flag = True
	for j in n:
		if j in p:
			nP = nP + j
			flag = False
	if flag:
		print(-1)
	else:
		print(nP)