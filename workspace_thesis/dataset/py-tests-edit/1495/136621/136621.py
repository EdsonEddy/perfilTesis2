import math
def fibo(x):
    fib=[]
    a, b = 0, 1
    for i in range(x):
        a, b = b,b+a
        fib.append(a)
    return(fib)
  
def trib(y):
	tri = [1]
	a, b, c	= 1, 3, 6 
	for i in range(y-1):
		a,b,c = b,c,c+b+a
		tri.append(a)
	return(tri)
	
def prim(z):
	pri = []
	for i in range(2,1000):
		for j in range(2,i):
			if i%j ==0:
				break
		else:
			pri.append(i)
		if len(pri) == z:
			return(pri)
while True:
	y, x = map(int,input().split())
	f, t, p, s, c = fibo(y), trib(y), prim(y),0,1
	s = float(s)
	for i in range(0,y):
		c+=1
		op = (t[i]*(math.pow(x,p[i]))/f[i])
		if c%2 != 0:
			s = s-op
		else:
			s = s+op
	print('{:.2f}'.format(s))