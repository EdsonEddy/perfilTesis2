from math import sqrt
def esprimo(nx):
	nx=int(nx)
	if nx !=1 and nx != 0:
		l=int(sqrt(nx)+1)
		for k in range(2,l,1):
			if nx%k==0:
				r='false'
				break
		else:
			r='true'
	else:
		r='false'
	return r	
	
def nprimo(y):
	yl=list(y)
	nn=' '
	for j in yl:
		if esprimo(j)=='true':
			nn=nn+j
	return nn
n= int(input())
for i in range(n):
	x=input()
	a=nprimo(x)
	if a==' ':
		print(-1)
	else:
		print(int(a))