while 1:
	n=int(input())
	c=0
	for i in range(n):
		a=input()
		aa=a[::-1]
		if a==aa:
			c+=1
	print(c)