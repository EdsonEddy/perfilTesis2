import sys 
for i in sys.stdin:
	c=0
	for j in range(int(i)):
		c+=int(input())
	print(c)