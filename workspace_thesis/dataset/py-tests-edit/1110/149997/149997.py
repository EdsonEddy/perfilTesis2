sw = True
for c in input():
	if not c in ['a', 'r', ' ']:
		sw = False
		break
print('Chewbacca' if sw == True else 'Han Solo')