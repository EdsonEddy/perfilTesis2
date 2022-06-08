import math
k=int(input())
for i in range(1,k+1,1):
	n=int(input())
	h=int(math.log(n,10))
	z=0
	while n>0:
		d=n//(pow(10,h))
		n=n%(pow(10,h))
		h=h-1
		if d==2 or d==3 or d==5 or d==7:
			z=(z*10)+d
	print(z)