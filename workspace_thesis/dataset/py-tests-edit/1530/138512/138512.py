t = int(input())
for i in range(t):
	n = int(input())
	c = 0
	a = 1
	while(n):
		d = n % 10
		if(d==2 or d==3 or d==5 or d==7):
			c = a*d + c
			a *= 10
		n = n // 10
	print(c)
