def fibo(n):
	a,b,c=1,0,0
	for i in range(n):
		c=a+b
		a=b
		b=c
	return c
x=int(input())
a=2
i=1
while i<=x/2:
	print(fibo(i))
	print(a)
	a+=2
	i+=1
if x&1==1:
	print(fibo(i))
