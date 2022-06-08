import math
n , k = map(int, input().split())
b = cd = int(math.log10(n)) + 1 
aux = 0

while n > 0:
	d = n // (10**(cd - 1))
	aux += 1     
	n = n % (10**(cd - 1))
	cd = cd - 1
	if aux == k:
		a = d
		break

print(b,a)
	
	 