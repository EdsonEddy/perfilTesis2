from math import *
cas=int(input())
while cas>0:
	n=int(input())
	a=n
	s=0
	while n>0:
		d=n%10
		n=n//10
		s=s+factorial(d)
	if s==a:
		print("Y")
	else:
		print("N")
	cas-=1