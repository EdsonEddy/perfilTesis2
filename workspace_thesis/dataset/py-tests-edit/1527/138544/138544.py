t = int(input())
for i in range(t):
	sw = 0
	n = int(input())
	while(n>9):
		if(n%100==96):
			sw = 1
		n = n // 10
	if(sw==0):print('TE SALVAS :D')
	else:print('APLAZADO!')
