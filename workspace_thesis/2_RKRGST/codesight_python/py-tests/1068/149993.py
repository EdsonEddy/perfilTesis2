for _ in range(0, int(input())):
	sw = True
	c = 0
	for _ in range(0, int(input())):
		if input() == 'porque':
			sw = False
		if sw == True:
			c += 1
	print(c)