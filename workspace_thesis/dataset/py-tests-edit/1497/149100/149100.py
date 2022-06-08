import string
pal = input()
lis = []
for i in pal:
	d = (ord(i))
	lis.append('{0:08b}'.format(d))
print(*lis,sep='')