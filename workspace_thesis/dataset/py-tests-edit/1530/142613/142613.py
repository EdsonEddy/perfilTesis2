from math import *
t=int(input())
for i in range(t):
	n=int(input())
	p=1
	nn=0
	while n>0:
		d=n%10
		n//=10
		if d==2 or d==3 or d==5 or d==7:
			nn+=d*p
			p*=10
	print(nn)


