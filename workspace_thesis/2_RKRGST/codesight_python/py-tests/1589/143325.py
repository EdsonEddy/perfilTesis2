cad = 'abcdefghijklmnopqrstuvwxyz'
s = input()
sw = 1
for c in cad:
	if(c not in s):
		sw = 0
		print(c)
		break
if(sw):print(-1)