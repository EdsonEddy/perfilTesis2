from sys import *
for line in stdin:
	a,b=map(int,line.split())
	l=int(b)
	if (l*(l+1)>>1)<=int(a):
		print("posible")
	else:
		print("imposible")