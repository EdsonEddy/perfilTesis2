import math
def esprimo(n):
	if n < 2:
		return False

	for i in range(2, (int(math.sqrt(n)+1))):
		if 	(n % i == 0):
			return False
	return True


while True:
	a = input()
	if a == '':
		break
	else:
		b = int(a)
		if(esprimo(b)):
			print ("ES PRIMO")
		else:
			print ("NO ES PRIMO")