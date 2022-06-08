import math
n = int(input(''))
while n>0:
	cont = True
	while cont:
		a, b = map(int, input().split())
		if a>=2 and b>=2 and a <= math.pow(10, 9) and b<= math.pow(10, 9):
			cont = False
	resto = 0
	while b > 0:
		resto = b
		b = a % b
		a = resto
	n = n -1
	print(a)