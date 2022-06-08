from sys import stdin
def palindromo(nu):
	num=0
	sw=False
	nuevo=nu
	while nu>0:
		d=nu%10
		nu=nu//10
		num=num*10+d
		if(nuevo==num):
			sw=True
	return sw

def contar(n):
	c=0
	for i in range(n):
		x=int(input())
		if palindromo(x):
			c=c+1
	print (c)

for n in stdin:
	n=int(n)
	contar(n)
