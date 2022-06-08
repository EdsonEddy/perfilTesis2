def fibo(numero):
	a=0
	b=1
	c=0
	if(numero==1):
		return 1
	for i in range(1,numero,1):
		c=a+b
		a=b
		b=c
	return c
numero=int(input())
while True:
   print( fibo(numero))
   numero = int(input())