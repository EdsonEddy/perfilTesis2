def felicidad(n):
	og = n
	c = 1
	while og!=0:
		l = list(map(int,str(n)))
		s = 0
		c += 1
		for i in l:
			s = s+(i**2)
		if c>8:
			return False
			og = 0
		elif s==1:
			return True
			og = 0
		n = s
rep = int(input())
for i in range(0,rep):
	n = int(input())
	if felicidad(n)==True:
		print('Feliz')
	else:
		print('Triste')