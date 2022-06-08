def invierte(n):
	m=0
	while n>0:
		d=n%10
		m=(m*10)+d
		n=n//10
	return m
def palin(n):
	m=invierte(n)
	if m==n:
		return True
	else:
		return False
		
while True:
	n=int(input())
	c=0
	for i in range(1,n+1,1):
		b=int(input())
		if palin(b):
			c=c+1
	print(c)
	c=0