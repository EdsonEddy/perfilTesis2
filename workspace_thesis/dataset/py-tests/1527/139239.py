import math
x=int(input())
for i in range(x):
	a=int(input())
	c=int(math.log10(a))
	if c==0:
		print("TE SALVAS :D")
	else:
		sw=True
		while sw and c>0:
			n=a//(10**(c-1))
			if n==96:
				sw=False
				break
			else:
				d=a//10**c
				a=a%10**c
				c=c-1
		if sw:
			print("TE SALVAS :D")
		else:
			print("APLAZADO!")