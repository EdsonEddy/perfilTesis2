n = int(input())
c = 1
while(n):
	a = '-'*n
	b = str(c)*((c-1)*2 + 1)
	print(a+b+a)
	n -= 1
	c += 1
