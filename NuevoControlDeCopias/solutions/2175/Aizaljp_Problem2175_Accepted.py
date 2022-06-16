contador=0
posicion=1
for i in range(int(input())):
	n=int(input())
	a=1
	b=0
	c=1
	if n==0:
		print(n)
	elif n==1:
		print(posicion)
	else:
		while c<n:
			c=a+b
			a=b
			b=c
			contador=contador+1
		if c==n:
			print(contador)
		contador=0
