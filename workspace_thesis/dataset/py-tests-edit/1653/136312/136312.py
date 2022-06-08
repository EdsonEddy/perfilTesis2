from sys import *
for line in stdin:
	a,b=map(int,line.split())
	if a%b==0 or b%a==0:
		print("PRIMOS ENEMIGOS")
	else:
		print("PRIMOS AMIGOS")
	
