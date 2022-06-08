palabra = input()
su  = []
for i in range(len(palabra)):
	su.append(palabra[i:])
su.sort()
for i in su:
	print(i)