n = int(input())
sw = True
while n > 0:
	if 7 != n%10 != 4:
		sw = False
	n //= 10
print('S' if sw == True else 'N')