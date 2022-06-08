import string
while True:
	n, k = map(str,input().split())
	n = int(n)
	kad = []
	for i in k:
		c = 0
		if i == '_':
			kad.append(' ')
		elif i not in string.ascii_lowercase:
			kad.append(i)
		else:
			le = string.ascii_lowercase.index(i) + n
			r = le%26
			for j in range(0,r):
				c = c+1
				if c>=26:
					c = 0
			kad.append(string.ascii_lowercase[c].upper())
	print(*kad,sep='')