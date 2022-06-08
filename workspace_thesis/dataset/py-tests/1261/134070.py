n =int(input())
for i in range(n):
	#Casos de prueba
	a, b =map(int,input().split())
	if b>=0:
		c=a**b
	print(c)