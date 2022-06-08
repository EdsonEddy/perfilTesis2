vocales = ['a','A','e','E','i','I','o','O','u','U','y','Y']
cad = input()
for i in cad:
	if i not in vocales:
		print('.',i.lower(),sep='', end='')