from sys import *
for line in stdin:
	l=int(line)
	ll=l
	r=0
	while l>0:
		r+=(l%10)
		l//=10
	print("La suma de los digitos de {} es {}".format(ll,r))
