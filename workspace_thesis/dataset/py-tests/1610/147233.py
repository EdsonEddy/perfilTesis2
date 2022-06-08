b = input()
c,l = 0,[]
for i in b:
	if i == '1':
		c = c+1
	elif i == '0':
		l.append(c)
		c = 0
l.append(c)
print(*l,sep='')