n = int(input())

for i in range (1,n+1):
	a, b = map(int, input().split())
	c = 1
	while c !=0:
		c = a%b
		if c ==0:
			break
		a = b 
		b = c
	print(b)