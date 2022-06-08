fi = [0]*(100000)

def fibo(n):
	if(n == 0 or n == 1):
		return 1
	if fi[n] != 0 :
		return fi[n]	
	c = fibo(n-1)+fibo(n-2)
	fi[n] = c
	return c

def pares(n):
	return n*2


fi[0]=1
fi[1]=1

a  = int(input())
c1 = 0
c2 = 1
sw = 1

while a != 0:
	a = a - 1
	if sw & 1:
		print(fibo(c1))
		c1 = c1 + 1
		sw = 0
	else:
		print(pares(c2))
		c2 = c2 + 1
		sw = 1
