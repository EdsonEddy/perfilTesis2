table = { ' ' : '%20', '!' : '%21', '$' : '%24', '%' : '%25', '(' : '%28', ')' : '%29', '*' : '%2a' }
s = input()
while s != '#':
	for c in s:
		if c in table.keys():
			print(table[c], end='')
		else:
			print(c, end='')
	print()
	s = input()