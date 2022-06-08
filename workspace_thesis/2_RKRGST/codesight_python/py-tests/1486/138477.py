def fibo (x):
	a,b=1,0
	for i in range (x):
		a,b=b,a+b
	return b
n=int(input())
x,y=2,1
for i in range (1,n+1):
	if i%2==0:
		print(x)
		x=x+2
	else:
		print(fibo(y))
		y+=1