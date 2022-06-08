def serie(n):
	a,b=1,0
	d=0
	x=0
	for i in range(n):
		if i%2==0:
			f=a+b
			a,b=b,f
			print(f)
		else:
			x+=2
			print(x)
n=int(input())
serie(n)