a, b, c = [int(x) for x in input(). split ()]
contador = 0
for i in range(a, b, c + 1):
	if i % 2 == 0:
		contador += 1


x, y, z = [int(x) for x in input(). split ()]
contador = 0
for i in range(x, y, z + 1):
	if i % 2 == 0:
		contador += 1



if x==(5-a) and y==(5-b) and z==(5-c):
	print("Esta es la llave")
else:
	print("Intenta con otra")