import sys
def mn(x):
	s ='abcdefghijklmnopqrstuvwxyz'
	c = 0
	for i in s:
		if(i==x):
			return c
		c += 1
	return -1
def my(x):
	s ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	c = 0
	for i in s:
		if(c==x):
			return i
		c += 1
	return 'A'
z = 'abcdefghijklmnopqrstuvwxyz'
for x in sys.stdin:
	n, s = x.split(' ')
	n = int(n)
	for i in s:
		if(i=='\n'):
			break
		if(i in z):
			print(my( (mn(i)+n) % 26),end='')
		elif(i=='_'):print(' ',end='')
		else:print(i,end='')
	print()
